import pip._vendor.requests as requests
import json
from opencage.geocoder import OpenCageGeocode
from haversine import haversine, Unit

def find_iss():
    # My Location ( Demo Times Sqaure)
    my_latitude=40.758896
    my_logtitude= -73.985130
    opencagecanada_api_key= "4e3b4cfa684943fd9f84df8158e6c626"
    iss_coordinates_api="http://api.open-notify.org/iss-now.json"
    
    response = requests.get(iss_coordinates_api)
    data = json.loads(response.text)

    for key,value in data.items():
        if key == 'iss_position':
            coordinates=value
            iss_latitude=coordinates['latitude']
            iss_longitude=coordinates['longitude']
            distance= haversine((float(iss_latitude), float(iss_longitude)),(float(my_latitude), float(my_logtitude)))
            geolocation  = find_iss_location(float(iss_latitude), float(iss_longitude),opencagecanada_api_key)
            print(f"Distance from Times Square",round(distance), "kms")
            print(f"ISS is above the geolocation", geolocation[0]['components'])

            if distance < 2:
                print("ISS is flying over you")

def find_iss_location(iss_latitude,iss_longitude, opencagecanada_api_key):
    geocoder = OpenCageGeocode(opencagecanada_api_key)
    result = geocoder.reverse_geocode(iss_latitude,iss_longitude)
    return result

find_iss()

