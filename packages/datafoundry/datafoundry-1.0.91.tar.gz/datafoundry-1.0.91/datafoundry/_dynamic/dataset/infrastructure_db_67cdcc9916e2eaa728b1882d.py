from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class infrastructure_db(DatasetBase):
    """
    Database: infrastructure_db
    Description: testing
   
    """
    def __init__(self):
        pass
        
    
    class campaign_db(TableBase):
        """
        Database: infrastructure_db
        Description: campaign db testing        
        """
        @classmethod
        def get_db_name(cls):
            return "infrastructure_db"

        @classmethod
        def get_table_name(cls):
            return "campaign_db"
    
# --- gen code block ---