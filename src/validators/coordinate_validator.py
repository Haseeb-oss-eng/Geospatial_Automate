import geopandas as gpd

class CoordinateValidator:
    def validate_input_data(self,gdf:gpd.GeoDataFrame):
        is_geodataframe = False
        if not isinstance(gdf,gpd.GeoDataFrame):
            raise ValueError("The Input Data is not GeoDataFrame")
        else:
            is_geodataframe = True
        return is_geodataframe
    
    def tocrs_epsg4326(self,gdf:gpd.GeoDataFrame):
        gdf = gdf.to_crs("EPSG:4326")  
        return gdf

    def check_crs(self,gdf:gpd.GeoDataFrame):
        is_crs_4326 = False
        if gdf.crs != "EPSG:4326":
            print(f"The Data not is in EPSG:4326")
            print("Converting to epsg:4326")
            self.tocrs_epsg4326(gdf)
            if gdf.crs == "EPSG:4326":
                is_crs_4326 = True
        else:
            is_crs_4326 = True

        return is_crs_4326

    def is_geom_valid(self,gdf:gpd.GeoDataFrame):
        is_valid = False
        if not gdf.is_valid():
            print(f"Geometry is not valid because: {gdf.is_valid_reason()}")
            raise TypeError("Geometry is not valid")
        else:
            is_valid = True

        return is_valid
    

    def check_all_aspect(self,gdf:gpd.GeoDataFrame):
        validated = False

        if self.validate_input_data(gdf):
            if self.check_crs(gdf):
                if self.is_geom_valid(gdf):
                    validated = True
                    print("Geometry is Valid")

        return validated


        
