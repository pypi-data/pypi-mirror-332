from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class newds(DatasetBase):
    """
    Database: newds
    Description: abc
   
    """
    def __init__(self):
        pass
        
    
    class abc(TableBase):
        """
        Database: newds
        Description: a        
        """
        @classmethod
        def get_db_name(cls):
            return "newds"

        @classmethod
        def get_table_name(cls):
            return "abc"
    
# --- gen code block ---