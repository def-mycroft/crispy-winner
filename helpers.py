"""Misc functions for app"""
import zipcode_tools

def read_csv(filename):
    """Reads a single column csv into a list"""
    output = list()
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            output.append(line)
    return output


def get_lat_lon(filename):
    """Returns two lists for lats and lons"""
    zipcodes = read_csv(filename)
    lats = list(); lons = list()
    for zipcode in zipcodes:
        data = zipcode_tools.get_city_data_geolocator(zipcode) 
        lats.append(data[0]); lons.append(data[1])
    return lats, lons
