import urllib.request
import json
from pprint import pprint

MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


MAPQUEST_API_KEY = 'KYYMLrlTQ397sa7pC47VMGXfwLWATIiT'
MBTA_API_KEY = '78d4e7adff704c049b5734452627c004'


def get_json(url):
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return(response_data)


def get_lat_long(place_name):
    place = place_name.replace(' ', '%20')
    url = f'{MAPQUEST_BASE_URL}?key={MAPQUEST_API_KEY}&location={place}'
     # print(url) # uncomment to test the url in browser
    place_json = get_json(url)
    # pprint(place_json)
    lat = place_json["results"][0]["locations"][0]['latLng']['lat'] 
    lon = place_json["results"][0]["locations"][0]['latLng']['lng']

    return lat, lon
    
def get_nearest_station(latitude, longitude):

    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    # print(url) # uncomment to test the url in browser
    station_json = get_json(url)
    # pprint(station_json) # uncomment to see the json data
    station_name = station_json["data"][0]["attributes"]["name"] # modify this so you get the correct station name
    print(station_name) # uncomment to check it

    # try to find out where the wheelchair_boarding information is
    wheelchair_boarding = station_json["data"][0]["attributes"]["wheelchair_boarding"]

    return station_name, wheelchair_boarding

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    You don't need to modify this function
    """
    return get_nearest_station(*get_lat_long(place_name))


def main():
    # final test here
    place = input('Enter a place name in Boston such as "Fenway Park": ')
    lat, lon = get_lat_long(place)
    #print(lat, lon)
    print(get_nearest_station(lat, lon))

    # final wrap-up
    print(find_stop_near(place))


if __name__ == '__main__':
    main()
