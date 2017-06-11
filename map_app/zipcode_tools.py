"""Two ways to get latlon data from a given zipcode string."""
import zipcode
from pyzipcode import ZipCodeDatabase # Can't import this for some reason.
from geopy.geocoders import Nominatim


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


def get_city_data_geolocator(zipc):
    """Given a zip code, return latlon and city name"""
    geolocator = ZipCodeDatabase()
    try:
        zip_data = geolocator[str(zipc)]
        lat = zip_data.latitude
        lon = zip_data.longitude
        name = '%s, %s' % (zip_data.city, zip_data.state)
        return lat, lon, name

    except:
        return 'None', 'None', 'None'
