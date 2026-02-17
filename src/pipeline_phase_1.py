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

def read_csvfile(csvFilePath):
    if csvFilePath.endswith('.csv'):
        return pd.read_csv(os.path.join(BRONZE_DIR, csvFilePath), sep=None)
    else:
        raise ValueError("File is not a CSV (.csv)")

def read_shapefile(shapefilePath):
    if shapefilePath.endswith('.shp'):
        return gpd.read_file(os.path.join(BRONZE_DIR, shapefilePath))
    else:
        raise ValueError("File is not a shapefile (.shp)")




def main():
    dataPath = os.listdir(BRONZE_DIR)
    shpfile  = [f for f in dataPath if f.endswith('.shp')]
    csvfile  = [f for f in dataPath if f.endswith('.csv')]

    if len(shpfile) > 0:
        gdf = read_shapefile(shpfile[0])
        print("Shapefile loaded successfully.")
        print_info(gdf)
        print(f"Shapefile CRS: {gdf.total_bounds}")
    else:
        print("No shapefile found in the bronze directory.")
    
    if len(csvfile) > 0:
        df = read_csvfile(csvfile[0])
        print("CSV file loaded successfully.")
        print_info(df)
        print(f"Minimum latitude value: {df['latitude'].min()}")  # Print minimum values for numeric columns
        print(f"Minimum longitude value: {df['longitude'].min()}")
        print(f"Maximum latitude value: {df['latitude'].max()}")  # Print maximum values for numeric columns
        print(f"Maximum longitude value: {df['longitude'].max()}")

    else:        
        print("No CSV file found in the bronze directory.")
    
    

if __name__ == "__main__":
    main()
