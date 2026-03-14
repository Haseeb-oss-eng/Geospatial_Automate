import pandas as pd
import geopandas as gpd

class GeoParquet:

    def write(self,gdf:gpd.GeoDataFrame,path):

        return gdf.to_parquet(path)