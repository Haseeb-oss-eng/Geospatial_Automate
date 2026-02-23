import geopandas as gpd

class PointBuilder:
    def build(self, df, lon_col="longitude", lat_col="latitude", crs="EPSG:4326"):
        if lon_col not in df.columns or lat_col not in df.columns:
            raise ValueError("Longitude/Latitude columns missing")

        return gpd.GeoDataFrame(
            df,
            geometry=gpd.points_from_xy(df[lon_col], df[lat_col]),
            crs=crs
        )
