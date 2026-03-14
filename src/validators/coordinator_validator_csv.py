import geopandas as gpd

class CoodinatorValidatorCSV:

    def check_geom(self,csvFile:gpd.GeoDataFrame):
        geom_field = True
        if not isinstance(csvFile,gpd.GeoDataFrame):
            return TypeError("File is not in GeoDataFrame Type")
        
        if not csvFile.latitude and csvFile.longitude:
            return ValueError("CSV Geospatial File doesn't contain latitude and longitude")
        
        return geom_field
        
    def check_latitude(self, csvFile:gpd.GeoDataFrame):
        return ((csvFile.latitude >= -90) & (csvFile.latitude <= 90)).all()
        
    def check_longitude(self, csvFile:gpd.GeoDataFrame):
        return ((csvFile.longitude >= -180) & (csvFile.longitude <= 180)).all()
    
    def check_all_aspect_csv(self,csvFile:gpd.GeoDataFrame):
        validated = False
        if self.check_geom(csvFile) and self.check_latitude(csvFile) and self.check_longitude(csvFile):
            validated = True
            return validated