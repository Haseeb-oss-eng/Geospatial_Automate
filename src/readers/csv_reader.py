import pandas as pd

#read the csv file

class CsvReader:

    def read_csvfile(self, file_path:str) -> pd.DataFrame:
        data = None
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return data