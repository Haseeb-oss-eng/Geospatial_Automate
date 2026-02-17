import os
from info.info import InfoPrinter
from readers.formatter import read
from geometry.point_builder import PointBuilder

# Bronze layer: raw data ingestion and print information about the data.
BRONZE_DIR = "/workspaces/Geospatial_Automate/data/bronze"
INFO_PRINTER = InfoPrinter()
spark = read()

def run():
    for file in os.listdir(BRONZE_DIR):
        file_path = os.path.join(BRONZE_DIR, file)
        if file.endswith('.csv'):
            data = spark.format('csv', file_path)
            print(f"CSV file metadata: {file}")
            INFO_PRINTER.print_info(data)
            #convert csv to geodataframe
            point_builder = PointBuilder()
            gdf_csv = point_builder.build_geodataframe(data)
            print(f"Geodataframe metadata from csv to gdf: {file}")
            INFO_PRINTER.print_info(gdf_csv)

        elif file.endswith('.shp'):
            gdf_csv = spark.format('shp', file_path)
            INFO_PRINTER.print_info(gdf_csv)
        
        else:
            print(f"Unsupported file type: {file}")
