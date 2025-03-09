import geopandas as gpd
from geopandas import *

# Import base geopandas classes
from geopandas import GeoSeries as _GeoSeries
from geopandas import GeoDataFrame as _GeoDataFrame

# Import our base with geodesic functionality
from .base import GeoPandasBase

# Create our extended classes
class GeoSeries(_GeoSeries, GeoPandasBase):
    """GeoSeries with geodesic capabilities."""
    pass

class GeoDataFrame(_GeoDataFrame):
    """GeoDataFrame with geodesic capabilities."""
    _constructor_sliced = GeoSeries

__version__ = "0.1.3"
