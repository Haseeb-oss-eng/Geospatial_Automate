class InfoPrinter:

    def print_info(self, dataframe):
        print(f"Data shape: {dataframe.shape[0]} rows")
        print(f"Column Names: {dataframe.columns.tolist()}")
        print(f"Data Types: {dataframe.dtypes}")
        print(f"Data head:\n{dataframe.head()}")