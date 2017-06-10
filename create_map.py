import pickle_funcs as pk  # remove this after testing
import matplotlib.pyplot as plt
import matplotlib.cm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import helpers
import zipcode_tools


def create_image(filename):
    print('Generating lats, lons from zipcodes')
    lats, lons = helpers.get_lat_lon(filename)
    print('Drawing map background')
    westlimit = -127.53; southlimit = 24.17;
    eastlimit = -63.19; northlimit = 50.32
    mid_lat = abs(westlimit - eastlimit) * 0.5
    mid_lon = abs(northlimit - southlimit) * 0.5
    fig, ax = plt.subplots(figsize=(16,9))
    # c, l, i, h, f or None
    m = Basemap(
        resolution='f', projection='merc', lat_0=mid_lat,
        lon_0=mid_lon, llcrnrlon=westlimit, llcrnrlat=southlimit,
        urcrnrlon=eastlimit, urcrnrlat=northlimit)
    m.drawmapboundary(fill_color='#46bcec')
    m.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
    m.drawcoastlines()
    m.readshapefile('statesp020', 'statesp020')
    print('Generated map. Plotting...')
    x, y = m(lons, lats)
    m.plot(x, y, '.', markersize='8')
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = fig_size[0] * 4
    fig_size[1] = fig_size[1] * 4
    plt.rcParams["figure.figsize"] = fig_size
    plt.savefig('output.png', bbox_inches=0)
    print('Output file saved.')
