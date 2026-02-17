import geopandas as gpd

class ShpReader:

    def read_shpfile(self, file_path:str) -> gpd.GeoDataFrame:
        data = None
        try:
            data = gpd.read_file(file_path)
            return data
        except Exception as e:
            print(f"Error reading SHP file: {e}")
            return data