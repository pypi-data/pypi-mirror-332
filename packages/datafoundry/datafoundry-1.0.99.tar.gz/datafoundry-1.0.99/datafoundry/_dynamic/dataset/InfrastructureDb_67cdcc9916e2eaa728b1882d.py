from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class InfrastructureDb(DatasetBase):
    """
    Database: InfrastructureDb
    Description: testing
   
    """
    def __init__(self):
        pass
        
    
    class CampaignDb(TableBase):
        """
        Database: InfrastructureDb
        Description: campaign db testing        
        """
        @classmethod
        def get_db_name(cls):
            return "InfrastructureDb"

        @classmethod
        def get_table_name(cls):
            return "CampaignDb"
    
# --- gen code block ---