import geopandas as gpd

class PointBuilder:
    def __init__(self, latitude: float, longitude: float, crs: str = "EPSG:4326"):
        self.x = longitude
        self.y = latitude
        self.crs = crs
        
    def build(self,df) -> gpd.GeoDataFrame:
        return gpd.GeoDataFrame(df,
                                geometry=gpd.points_from_xy(df[self.x], df[self.y]),
                                crs=self.crs)
        