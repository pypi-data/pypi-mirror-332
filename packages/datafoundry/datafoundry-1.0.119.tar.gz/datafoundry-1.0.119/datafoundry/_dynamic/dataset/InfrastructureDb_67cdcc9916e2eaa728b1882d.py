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
            return "infrastructuredb"

        @classmethod
        def get_table_name(cls):
            return "campaigndb"
    
    class Marketing(TableBase):
        """
        Database: InfrastructureDb
        Description: vng marketing dataset        
        """
        @classmethod
        def get_db_name(cls):
            return "infrastructuredb"

        @classmethod
        def get_table_name(cls):
            return "marketing"
    
    class MarketingV2(TableBase):
        """
        Database: InfrastructureDb
        Description: marketing        
        """
        @classmethod
        def get_db_name(cls):
            return "infrastructuredb"

        @classmethod
        def get_table_name(cls):
            return "marketingv2"
    
    class MarketingV3(TableBase):
        """
        Database: InfrastructureDb
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "infrastructuredb"

        @classmethod
        def get_table_name(cls):
            return "marketingv3"
    
# --- gen code block ---