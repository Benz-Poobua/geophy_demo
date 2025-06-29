# GitHub & Seismology Workshop: 2024 Hualien Earthquake Analysis
In this workshop, we will investigate one of the most significant recent seismic events: the 2024 Hualien Earthquake, which struck eastern Taiwan with a moment magnitude of 7.4. You will learn how to retrieve seismic data, process it with Python, and manage your project using Git and GitHub, specifically with GitHub Desktop for ease of use.

## Background: 2024 Hualien Earthquake, Taiwan
### Date & Time
- UTC: April 3, 2024, at 23:58:10 UTC
- Local time: April 4, 2024, around 07:58 AM (Taiwan Standard Time)

### Location & Tectonic Setting
- Epicenter: Near Hualien, on the eastern coast of Taiwan
- Coordinates: Approximately 23.8°N, 121.6°E
- Depth: ~40 km

Taiwan is located at the convergent boundary between the Eurasian Plate and the Philippine Sea Plate, where complex tectonic interactions lead to frequent seismic activity. The eastern region, including Hualien, is especially seismically active due to ongoing collision and subduction processes.

### Magnitude and Rupture
- Moment Magnitude (Mw): 7.4
- One of the strongest earthquakes in Taiwan in the past 25 years
- Likely involved reverse faulting (thrust fault) based on moment tensor solutions

### 2024 Hualien Earthquake Summary

| Parameter               | Description                                                      |
|------------------------|------------------------------------------------------------------|
| **Date (UTC)**         | April 3, 2024, 23:58:10                                          |
| **Local Time (TST)**   | April 4, 2024, 07:58 AM                                          |
| **Magnitude**          | Mw 7.4                                                           |
| **Epicenter Location** | Near Hualien, Taiwan                                             |
| **Coordinates**        | 23.8°N, 121.6°E                                                  |
| **Depth**              | 40km                                                             |
| **Faulting Mechanism** | Likely thrust faulting (reverse), based on moment tensor         |
| **Tectonic Setting**   | Convergent boundary between Philippine Sea Plate and Eurasian Plate |
| **Impact**             | Strong shaking, infrastructure damage, landslides, aftershocks   |
| **Notable Aftershocks**| Several M6+ aftershocks within hours/days                        |
| **Agencies**           | USGS, Taiwan CWB, GFZ, IRIS                                      |

![Taiwan](https://github.com/Benz-Poobua/Hualien-Earthquake-analysis/blob/cdd728d53e5d598b40661baaff6c81366399deca/unw-taiwan.png?raw=true)

### Seismogram modeling
The seismogram you record, denoted as **s(t)**, is the result of multiple convolution operations representing different components in the seismic wave propagation system:

$$
s(t) = x(t) * e(t) * q(t) * i(t)
$$

### Installation Instructions
**For `pip` users**
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# (Optional) Register Jupyter kernel
python -m ipykernel install --user --name=geophy_demo --display-name "geophy_demo"
```
**For `conda` users**
```bash
# Create the environment from the YAML file
conda env create -f environment.yml

# Activate the environment
conda activate geophy_demo

# (Optional) Register Jupyter kernel
python -m ipykernel install --user --name=geophy_demo --display-name "geophy_demo"
```
