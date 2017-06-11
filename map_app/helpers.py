"""Misc functions for app"""
from . import zipcode_tools
import re

def to_csv(alist):
    with open('errors.csv', 'w+') as f:
        for line in alist:
            f.write('%s,\n' % line)


def get_lat_lon(df, col='ZipCode'):
    """Returns two lists for lats and lons"""
    lats = list(); lons = list(); errors = list();
    for zipcode in df[col]:
        data = zipcode_tools.get_city_data_geolocator(zipcode) 
        lat = data[0]; lon = data[1];
        if isinstance(lat, float) and isinstance(lon, float):
            lats.append(lat); lons.append(lon)
        else:
            errors.append(zipcode)
    if len(errors) != 0:
        to_csv(errors)
        print('Errors written to file. Length: %s' % len(errors))
    return lats, lons


def find_zip_code(astring):
    """Uses regex to find zipcode in a string"""
    regex = r'\d{5}'
    zipcode = re.findall(regex, str(astring))
    if len(zipcode) != 0:
        return zipcode[0]
    else:
        return 'NA'
