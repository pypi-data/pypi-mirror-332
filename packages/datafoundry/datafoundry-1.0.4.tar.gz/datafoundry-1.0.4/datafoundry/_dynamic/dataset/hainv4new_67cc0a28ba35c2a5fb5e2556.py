from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class hainv4new(DatasetBase):
    """
    Database: hainv4new
    Description: This is analytics dataset
   
    """
    def __init__(self):
        pass
        
    
    class campaigntable(TableBase):
        """
        Database: hainv4new
        Description: campaign channel table for test        
        """
        @classmethod
        def get_db_name(cls):
            return "hainv4new"

        @classmethod
        def get_table_name(cls):
            return "campaigntable"
    
# --- gen code block ---