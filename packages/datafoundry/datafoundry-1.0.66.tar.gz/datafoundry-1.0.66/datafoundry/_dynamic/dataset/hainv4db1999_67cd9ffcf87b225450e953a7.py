from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class hainv4db1999(DatasetBase):
    """
    Database: hainv4db1999
    Description: abc
   
    """
    def __init__(self):
        pass
        
    
    class hainv4table99(TableBase):
        """
        Database: hainv4db1999
        Description: abc        
        """
        @classmethod
        def get_db_name(cls):
            return "hainv4db1999"

        @classmethod
        def get_table_name(cls):
            return "hainv4table99"
    
# --- gen code block ---