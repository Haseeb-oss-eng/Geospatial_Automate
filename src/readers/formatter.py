from readers.shp_reader import ShpReader
from readers.csv_reader import CsvReader

class ReaderFactory:
    def read(self, file_type: str, file_path: str):
        if file_type == 'shp':
            return ShpReader().read_shpfile(file_path)
        elif file_type == 'csv':
            return CsvReader().read_csvfile(file_path)
        else:
            raise ValueError("Unsupported file type")
    
        