# ISS Tracker

This Python script tracks the current location of the International Space Station (ISS) and calculates the distance between the ISS and a specified location (by default, Times Square, New York). Additionally, the script uses reverse geocoding to identify the location over which the ISS is currently flying.

## Features

- **Fetch ISS Location**: Retrieves real-time ISS coordinates using the [Open Notify ISS API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/).
- **Haversine Distance Calculation**: Calculates the distance between the ISS and a specified location using the Haversine formula.
- **Geolocation Lookup**: Uses the [OpenCage Geocoder API](https://opencagedata.com/) to reverse geocode the ISS coordinates into a human-readable location.
- **Customizable Location**: The script can be easily modified to track the ISS distance from any location by updating the latitude and longitude coordinates.

## Requirements

To run this script, you need to install the following Python packages:

```bash
pip install requests opencage geocoder haversine
```

## Usage

- Clone the repository or download the script.
- Install the required dependencies.
- Get your API key from OpenCageData. Replace the placeholder API key in the script with your actual key.
- Update the `my_latitude` and `my_longitude` variables with the coordinates of your desired location (or leave it as Times Square for the demo).

## Output

The script will output the following:

- The distance between the ISS and the specified location.
- The geolocation of where the ISS is currently above.
- A message indicating if the ISS is flying directly overhead (within 2 km).

## Developer
- [Ranopriyo Neogy](https://github.com/ranopriyo-neogy)
