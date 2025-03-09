from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class DatasetTest(DatasetBase):
    """
    Database: DatasetTest
    Description: lorem ipsum promax
   
    """
    def __init__(self):
        pass
        
    
    class tbl32(TableBase):
        """
        Database: DatasetTest
        Description: lorem ipsum 111        
        """
        @classmethod
        def get_db_name(cls):
            return "DatasetTest"

        @classmethod
        def get_table_name(cls):
            return "tbl32"
    
# --- gen code block ---