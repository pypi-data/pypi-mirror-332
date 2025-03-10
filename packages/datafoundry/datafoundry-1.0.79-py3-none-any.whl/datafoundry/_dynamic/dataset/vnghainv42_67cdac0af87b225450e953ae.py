from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class vnghainv42(DatasetBase):
    """
    Database: vnghainv42
    Description: abc
   
    """
    def __init__(self):
        pass
        
    
    class table1(TableBase):
        """
        Database: vnghainv42
        Description: abccc        
        """
        @classmethod
        def get_db_name(cls):
            return "vnghainv42"

        @classmethod
        def get_table_name(cls):
            return "table1"
    
# --- gen code block ---