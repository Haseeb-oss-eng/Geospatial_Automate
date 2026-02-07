import pandas as pd
import geopandas as gpd

# Use the raw.githubusercontent URL (not the GitHub HTML/blob URL)
url = "https://raw.githubusercontent.com/opengeos/data/main/world/cities5000.csv"

# # Read with pandas and let the python engine sniff the delimiter (this file is tab-separated)
# df = pd.read_csv(url, sep=None, engine="python")

# # Find latitude and longitude columns (case-insensitive, robust to minor name differences)
# cols = {c.lower(): c for c in df.columns}
# lat_col = None
# lon_col = None
# for name in cols:
# 	if name.startswith("lat"):
# 		lat_col = cols[name]
# 	if name.startswith("lon") or name.startswith("long"):
# 		lon_col = cols[name]

# if lat_col is None or lon_col is None:
# 	raise ValueError(f"Could not find latitude/longitude columns in CSV. Columns: {list(df.columns)}")

# # Convert to numeric and drop rows with invalid coords
# df[lat_col] = pd.to_numeric(df[lat_col], errors="coerce")
# df[lon_col] = pd.to_numeric(df[lon_col], errors="coerce")
# df = df.dropna(subset=[lat_col, lon_col])

# # Create a GeoDataFrame
# gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[lon_col], df[lat_col]), crs="EPSG:4326")

# print(gdf.head())

print(pd.read_csv(url, sep=None, engine="python").head())