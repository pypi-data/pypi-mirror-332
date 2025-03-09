from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class haitest1(DatasetBase):
    """
    Database: haitest1
    Description: None
   
    """
    def __init__(self):
        pass
        
    
    class table1(TableBase):
        """
        Database: haitest1
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "haitest1"

        @classmethod
        def get_table_name(cls):
            return "table1"
    
# --- gen code block ---