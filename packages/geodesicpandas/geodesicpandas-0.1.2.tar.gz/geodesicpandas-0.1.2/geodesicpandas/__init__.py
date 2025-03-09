import geopandas as gpd
from geopandas import *

# Re-export base classes with geodesic functionality
from .base import GeoPandasBase
from .geoseries import GeoSeries
from .geodataframe import GeoDataFrame

__version__ = "0.1.2"
