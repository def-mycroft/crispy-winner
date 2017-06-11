from . import create_map
import imp


def map_image(filename):
    create_map.create_image(filename, imp.find_module('map_app')[1]+'/')

