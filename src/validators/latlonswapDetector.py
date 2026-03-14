import geopandas as gpd

class LatLonSwapDector:

    def detect(self, gdf:gpd.GeoDataFrame):
        swap = True
        possible_swap = gdf[(gdf.latitude.abs() > 90) & (gdf.longitude.abs() < 90)]
        count = len(possible_swap)
        if count > 0:
            print(f"⚠ Possible swapped coordinates detected: {count} rows")
        else:
            print("No swapped coordinates detected")
            swap = True

        return swap