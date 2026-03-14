import geopandas as gpd

class visualize:

    def map_it(self,gdf:gpd.GeoDataFrame):
        m = gdf.explore()
        # Save the map as an HTML file
        m.save("OutputMap/world_map.html")
