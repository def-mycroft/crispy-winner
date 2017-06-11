from setuptools import setup

setup(name='map_app',
      version='0.1',
      description='Given a set of zipcodes, plot representative points on map',
      url='https://github.com/def-mycroft/crispy-winner',
      author='Joseph Dasenbrock',
      author_email='dasenbrockjw@gmail.com',
      packages=['map_app'],
      package_data={'': ['statesp020.dbf',
                         'statesp020.shp', 'statesp020.shx', 'statesp020.txt']},
      zip_safe=False)
