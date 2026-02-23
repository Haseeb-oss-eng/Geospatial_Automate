import geopandas as gpd


class GeometrySanity:

    def check(self, gdf):
        if not isinstance(gdf, gpd.GeoDataFrame):
            raise TypeError("Input must be a GeoDataFrame")
        
        print("CRS:", gdf.crs)
        print("Geometry Types:", gdf.geometry.geom_type.unique())
        print("Geometry Validity:", gdf.geometry.isnull().sum(), "null geometries")
        print("Invalid geometries:", (~gdf.geometry.is_valid).sum())