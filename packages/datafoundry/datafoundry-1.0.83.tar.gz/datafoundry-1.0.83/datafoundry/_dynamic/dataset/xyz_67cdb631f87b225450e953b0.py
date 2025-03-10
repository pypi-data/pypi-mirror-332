from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class xyz(DatasetBase):
    """
    Database: xyz
    Description: abc
   
    """
    def __init__(self):
        pass
        
    
    class xyz(TableBase):
        """
        Database: xyz
        Description: xyz        
        """
        @classmethod
        def get_db_name(cls):
            return "xyz"

        @classmethod
        def get_table_name(cls):
            return "xyz"
    
# --- gen code block ---