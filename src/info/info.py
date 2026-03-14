class InfoPrinter:

    def print_info(self, dataframe):
        if hasattr(dataframe, "geometry"):
            print("Geometry type:", dataframe.geometry.geom_type.unique())
            print("CRS:", dataframe.crs)
        print(f"Data Types: {dataframe.dtypes}")