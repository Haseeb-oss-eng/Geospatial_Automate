import pandas as pd
import geopandas as gpd
import os

# Bronze layer: raw data ingestion
BRONZE_DIR = "/workspaces/Geospatial_Automate/data/bronze"
def print_info(dataframe):
    print(f"Data shape: {dataframe.shape[0]} rows")
    print(f"Column Names: {dataframe.columns.tolist()}")
    print(f"Data Types: {dataframe.dtypes}")
    print(f"Data head:\n{dataframe.head()}")

def csv_file(csvFilePath):
    if csvFilePath.endswith('.csv'):
        return pd.read_csv(os.path.join(BRONZE_DIR, csvFilePath), sep=None)
    else:
        raise ValueError("File is not a CSV (.csv)")

def shapefile(shapefilePath):
    if shapefilePath.endswith('.shp'):
        return gpd.read_file(os.path.join(BRONZE_DIR, shapefilePath))
    else:
        raise ValueError("File is not a shapefile (.shp)")

def main():
    dataPath = os.listdir(BRONZE_DIR)
    shpfile  = [f for f in dataPath if f.endswith('.shp')]
    csvfile  = [f for f in dataPath if f.endswith('.csv')]

    if len(shpfile) > 0:
        gdf = shapefile(shpfile[0])
        print("Shapefile loaded successfully.")
        print_info(gdf)
    else:
        print("No shapefile found in the bronze directory.")
    
    if len(csvfile) > 0:
        df = csv_file(csvfile[0])
        print("CSV file loaded successfully.")
        print_info(df)
    else:        
        print("No CSV file found in the bronze directory.")
    
    

if __name__ == "__main__":
    main()
