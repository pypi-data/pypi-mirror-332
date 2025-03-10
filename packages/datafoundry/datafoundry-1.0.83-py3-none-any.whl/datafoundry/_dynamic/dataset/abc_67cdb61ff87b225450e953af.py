from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class abc(DatasetBase):
    """
    Database: abc
    Description: abc
   
    """
    def __init__(self):
        pass
        
    
    class abc(TableBase):
        """
        Database: abc
        Description: add name        
        """
        @classmethod
        def get_db_name(cls):
            return "abc"

        @classmethod
        def get_table_name(cls):
            return "abc"
    
# --- gen code block ---