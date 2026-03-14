import os
from info.info import InfoPrinter
from readers.formatter import ReaderFactory
from geometry.point_builder import PointBuilder
from geometry.geometry_sanity import GeometrySanity
from validators.coordinate_validator import CoordinateValidator
from validators.coordinator_validator_csv import CoodinatorValidatorCSV
from visualize import visualize

# Bronze layer: raw data ingestion and print information about the data.
BRONZE_DIR = "/workspaces/Geospatial_Automate/data/bronze"
INFO_PRINTER = InfoPrinter()
GEOMETRY_SANITY = GeometrySanity()
COORDINATE_VALIDATOR = CoordinateValidator()
COORDINATE_VALIDATOR_CSV = CoodinatorValidatorCSV()
MAP = visualize()


def run():
    reader = ReaderFactory()
    point_builder = PointBuilder()

    for file in os.listdir(BRONZE_DIR):
        file_path = os.path.join(BRONZE_DIR, file)

        if file.endswith(".csv"):
            df_csv = reader.read("csv", file_path)
            INFO_PRINTER.print_info(df_csv)

            #validate the geometry
            gdf_valid_csv = COORDINATE_VALIDATOR_CSV.check_all_aspect_csv(df_csv)

            if gdf_valid_csv :
                gdf_csv = point_builder.build(df_csv)
                INFO_PRINTER.print_info(gdf_csv)

            # Check geometry sanity in csv files
            print("Checking geometry sanity for CSV file...")
            GEOMETRY_SANITY.check(gdf_csv)

        elif file.endswith(".shp"):
            gdf_shp = reader.read("shp", file_path)
            INFO_PRINTER.print_info(gdf_shp)

            #validate the geometry
            gdf_valid_shp = COORDINATE_VALIDATOR.check_all_aspect(gdf_shp)

            if gdf_valid_shp:
                # Check geometry sanity in shapefiles
                print("Checking geometry sanity for Shapefile...")
                GEOMETRY_SANITY.check(gdf_shp)
            
    return gdf_csv, gdf_shp

def map():
    csvmap, gdfmap = run()
    MAP.map_it(gdfmap)
