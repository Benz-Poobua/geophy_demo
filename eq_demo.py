from datetime import datetime

from obspy.taup import TauPyModel
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.geodetics import locations2degrees, gps2dist_azimuth

from libcomcat.search import search
from libcomcat.dataframes import get_summary_data_frame

### Step 1: Explore the event
events = search(starttime = datetime(2024, 4, 1, 0, 0), endtime = datetime(2024, 4, 3, 0, 0), minmagnitude = 6.5)
event_df = get_summary_data_frame(events)
print(event_df)

hualien_event = event_df[event_df.id == 'us7000m9g4']

# Define coordinates
event_lat, event_lon = hualien_event.latitude.to_numpy()[0], hualien_event.longitude.to_numpy()[0]
station_lat, station_lon = 24.974, 121.497  # TATO station


# Calculate distance in degrees using obspy
distance_deg = locations2degrees(event_lat, event_lon, station_lat, station_lon)

# Calculate distance, azimuth, and back-azimuth using obspy
distance_m, azimuth, back_azimuth = gps2dist_azimuth(event_lat, event_lon, station_lat, station_lon)

# Convert distance from meters to kilometers
distance_km_obspy = distance_m / 1000

print(f'Distance = {distance_km_obspy:.2f} km')
print(f'Distance = {distance_deg:.2f} degrees')
print(f'Azimuth (event to station) = {azimuth:.2f}°')
print(f'Back-azimuth (station to event) = {back_azimuth:.2f}°')

### Step 2: Visual the waveforms

# Create velocity model
model = TauPyModel(model = 'iasp91')

# Calculate travel times
arrivals = model.get_travel_times(
    source_depth_in_km = hualien_event.depth.to_numpy()[0], 
    distance_in_degree=distance_deg
)

# List all arrivals
print('Available seismic phases and arrival times:')
for arrival in arrivals:
    print(f'Phase: {arrival.name}, Arrival Time: {arrival.time:.2f} sec')

# Download seismic data
network = 'IU'
station = 'TATO'
channel = 'BH*'
starttime = UTCDateTime('2024-04-22T23:58:11')
endtime = starttime + 60 * 15 # 15 minutes window

client = Client('IRIS')

# Get waveform data with instrument response
st = client.get_waveforms(network=network, station=station, location='00', channel=channel, starttime=starttime, endtime=endtime, attach_response=True)

# Remove instrument response (convert to velocity)
st.remove_response(output='VEL')

# Basic preprocessing
st.merge(fill_value='interpolate')  # Merge traces if gaps
st.detrend(type='linear')           # Remove linear trend
st.taper(max_percentage=0.05)       # Apply taper

print(st)

# Plot the waveform
st[2].plot() # Plot only Z component

# Plot the spectrogram
st[2].spectrogram(log=True)

# Filter the waveform
tr = st[2].copy()
tr.filter('bandpass', freqmin=1.0, freqmax=5.0, corners=4, zerophase=True)
tr.plot()

# Save the seismogram for later use; `MSEED` format
tr.write("hualien.mseed", format="MSEED")

# Save the figure
fig = tr.plot(show=False)
fig.savefig('Waveform.png', dpi=300)


# !pip install pyrocko
# !snuffler hualien.mseed