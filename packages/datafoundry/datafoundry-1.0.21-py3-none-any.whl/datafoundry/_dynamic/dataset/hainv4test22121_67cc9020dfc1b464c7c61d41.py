from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class hainv4test22121(DatasetBase):
    """
    Database: hainv4test22121
    Description: None
   
    """
    def __init__(self):
        pass
        
    
    class campaign_table(TableBase):
        """
        Database: hainv4test22121
        Description: abc        
        """
        @classmethod
        def get_db_name(cls):
            return "hainv4test22121"

        @classmethod
        def get_table_name(cls):
            return "campaign_table"
    
# --- gen code block ---