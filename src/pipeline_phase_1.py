import pandas as pd
import geopandas as gpd
import os
from info.info import InfoPrinter
from readers.formatter import Formatter

# Bronze layer: raw data ingestion and print information about the data.
BRONZE_DIR = "/workspaces/Geospatial_Automate/data/bronze"
INFO_PRINTER = InfoPrinter()
Format = Formatter()

def main():
    dataPath = os.listdir(BRONZE_DIR)
    shpfile  = [f for f in dataPath if f.endswith('.shp')]
    csvfile  = [f for f in dataPath if f.endswith('.csv')]

    
    

if __name__ == "__main__":
    main()
