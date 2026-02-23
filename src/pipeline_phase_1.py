import os
from info.info import InfoPrinter
from readers.formatter import ReaderFactory
from geometry.point_builder import PointBuilder
from geometry.geometry_sanity import GeometrySanity 

# Bronze layer: raw data ingestion and print information about the data.
BRONZE_DIR = "/workspaces/Geospatial_Automate/data/bronze"
INFO_PRINTER = InfoPrinter()
GEOMETRY_SANITY = GeometrySanity()


def run():
    reader = ReaderFactory()
    point_builder = PointBuilder()

    for file in os.listdir(BRONZE_DIR):
        file_path = os.path.join(BRONZE_DIR, file)

        if file.endswith(".csv"):
            df = reader.read("csv", file_path)
            INFO_PRINTER.print_info(df)

            gdf = point_builder.build(df)
            INFO_PRINTER.print_info(gdf)

            # Check geometry sanity in csv files
            print("Checking geometry sanity for CSV file...")
            GEOMETRY_SANITY.check(gdf)

        elif file.endswith(".shp"):
            gdf = reader.read("shp", file_path)
            INFO_PRINTER.print_info(gdf)

            # Check geometry sanity in shapefiles
            print("Checking geometry sanity for Shapefile...")
            GEOMETRY_SANITY.check(gdf)