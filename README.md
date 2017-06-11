# Python Map Application
Python script which plots points on a map of the United States, given a list of zip codes. 

## Usage 

Install with below instructions. A Pandas DataFrame with a column titled 
'ZipCode' can be passed to the 'create\_map' function, imported from the 'map\_app' module.

## Installation Instructions 

For anaconda python 3, first run these commands:
```
conda install -c conda-forge basemap=1.0.8.dev0
conda install -c conda-forge basemap-data-hires
pip install zipcode
pip install geopy
```

Clone this repo, navigate to the cloned repo, and run:

`pip install .`
