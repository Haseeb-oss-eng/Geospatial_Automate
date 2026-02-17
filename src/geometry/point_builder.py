import geopandas as gpd

class PointBuilder:
        
    def build(self,df, crs: str = "EPSG:4326") -> gpd.GeoDataFrame:
        return gpd.GeoDataFrame(df,
                                geometry=gpd.points_from_xy(df["longitude"], df["latitude"]),
                                crs=crs)
        