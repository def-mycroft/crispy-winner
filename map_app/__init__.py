from . import map_generator
from . import zipcode_tools
import imp


def create_map(filename):
    map_generator.create_image(filename, imp.find_module('map_app')[1]+'/')

