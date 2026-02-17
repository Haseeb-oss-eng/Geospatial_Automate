from shp_reader import ShpReader
from csv_reader import CsvReader

class read:

    def __init__(self, ShpReader: ShpReader, CsvReader: CsvReader):
        self.ShpReader = ShpReader
        self.CsvReader = CsvReader

    def format(self, file_type:str, file_path:str):
        if file_type == 'shp':
            self.ShpReader.read_shpfile(file_path)
        elif file_type == 'csv':
            return self.CsvReader.read_csvfile(file_path)
        else:
            print("Unsupported file type")
            return None
    
        