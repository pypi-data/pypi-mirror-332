from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class DatasetTest(DatasetBase):
    """
    Database: DatasetTest
    Description: lorem ipsum
   
    """
    def __init__(self):
        pass
        
    
    class tbl_test(TableBase):
        """
        Database: DatasetTest
        Description: abdefv        
        """
        @classmethod
        def get_db_name(cls):
            return "DatasetTest"

        @classmethod
        def get_table_name(cls):
            return "tbl_test"
    
# --- gen code block ---