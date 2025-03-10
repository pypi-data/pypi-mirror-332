from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class zdatasethainv4(DatasetBase):
    """
    Database: zdatasethainv4
    Description: abc
   
    """
    def __init__(self):
        pass
        
    
    class ztablehainv4(TableBase):
        """
        Database: zdatasethainv4
        Description: abcccc        
        """
        @classmethod
        def get_db_name(cls):
            return "zdatasethainv4"

        @classmethod
        def get_table_name(cls):
            return "ztablehainv4"
    
# --- gen code block ---