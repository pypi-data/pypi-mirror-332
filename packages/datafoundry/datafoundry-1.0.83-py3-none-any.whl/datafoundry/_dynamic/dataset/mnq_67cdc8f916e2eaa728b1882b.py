from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class mnq(DatasetBase):
    """
    Database: mnq
    Description: mnq
   
    """
    def __init__(self):
        pass
        
    
    class mnq2(TableBase):
        """
        Database: mnq
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "mnq"

        @classmethod
        def get_table_name(cls):
            return "mnq2"
    
# --- gen code block ---