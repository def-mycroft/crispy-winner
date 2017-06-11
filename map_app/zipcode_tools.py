"""Zipcode tools - translate zipcodes into gps coordinates."""
import zipcode
from geopy.geocoders import Nominatim
from geopy.distance import great_circle


def get_city_data_geopy(zipc):
    """Given a zip code, return latlon and city name"""
    geolocator = Nominatim()
    coord_data = geolocator.geocode(str(zipc))
    name_data = zipcode.isequal(str(zipc))
    if coord_data is not None and name_data is not None:
        lat = coord_data[1][0]
        lon = coord_data[1][1]
        name = '%s, %s' % (name_data.city, name_data.state)
        return lat, lon, name
    # Some data points are empty, return string of none in this case
    else:
        return 'None', 'None', 'None'


def dist_between_zips(zipone, ziptwo):
    """Returns great-circle distance between two zip code"""
    zipone = get_city_data_geopy(zipone)
    ziptwo = get_city_data_geopy(ziptwo)
    if 'None' not in zipone and 'None' not in ziptwo:
        return great_circle(tuple(zipone[:2]), tuple(ziptwo[:2])).miles
    else:
        return 0
