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