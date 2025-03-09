from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class Hainv4test(DatasetBase):
    """
    Database: Hainv4test
    Description: test again
   
    """
    def __init__(self):
        pass
        
    
    class Haitest(TableBase):
        """
        Database: Hainv4test
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "Hainv4test"

        @classmethod
        def get_table_name(cls):
            return "Haitest"
    
# --- gen code block ---