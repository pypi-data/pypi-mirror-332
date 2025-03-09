from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class Haitest1(DatasetBase):
    """
    Database: Haitest1
    Description: None
   
    """
    def __init__(self):
        pass
        
    
    class Table1(TableBase):
        """
        Database: Haitest1
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "Haitest1"

        @classmethod
        def get_table_name(cls):
            return "Table1"
    
# --- gen code block ---