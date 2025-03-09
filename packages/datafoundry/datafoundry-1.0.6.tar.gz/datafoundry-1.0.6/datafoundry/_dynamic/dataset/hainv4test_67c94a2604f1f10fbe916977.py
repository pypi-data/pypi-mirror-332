from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class hainv4test(DatasetBase):
    """
    Database: hainv4test
    Description: test again
   
    """
    def __init__(self):
        pass
        
    
    class haitest(TableBase):
        """
        Database: hainv4test
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "hainv4test"

        @classmethod
        def get_table_name(cls):
            return "haitest"
    
# --- gen code block ---