from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class vnghainv4(DatasetBase):
    """
    Database: vnghainv4
    Description: test desc
   
    """
    def __init__(self):
        pass
        
    
    class table1(TableBase):
        """
        Database: vnghainv4
        Description: abc        
        """
        @classmethod
        def get_db_name(cls):
            return "vnghainv4"

        @classmethod
        def get_table_name(cls):
            return "table1"
    
# --- gen code block ---