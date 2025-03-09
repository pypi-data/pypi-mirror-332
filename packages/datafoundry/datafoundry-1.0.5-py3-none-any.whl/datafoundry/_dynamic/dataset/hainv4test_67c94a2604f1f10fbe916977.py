from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class hainv4test(DatasetBase):
    """
    Database: hainv4test
    Description: test
   
    """
    def __init__(self):
        pass
        
    
    class table12(TableBase):
        """
        Database: hainv4test
        Description: abc        
        """
        @classmethod
        def get_db_name(cls):
            return "hainv4test"

        @classmethod
        def get_table_name(cls):
            return "table12"
    
# --- gen code block ---