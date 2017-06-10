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


def to_csv(alist):
    with open('errors.csv', 'w+') as f:
        for line in alist:
            f.write('%s,\n' % line)


def get_lat_lon(filename):
    """Returns two lists for lats and lons"""
    zipcodes = read_csv(filename)
    lats = list(); lons = list(); errors = list();
    for zipcode in zipcodes:
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
