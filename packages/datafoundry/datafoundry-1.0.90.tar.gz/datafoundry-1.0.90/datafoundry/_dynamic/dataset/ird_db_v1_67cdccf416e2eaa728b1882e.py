from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class ird_db_v1(DatasetBase):
    """
    Database: ird_db_v1
    Description: abc
   
    """
    def __init__(self):
        pass
        
    
    class campaign_db_2(TableBase):
        """
        Database: ird_db_v1
        Description: desc        
        """
        @classmethod
        def get_db_name(cls):
            return "ird_db_v1"

        @classmethod
        def get_table_name(cls):
            return "campaign_db_2"
    
    class campaign_tbl_v2(TableBase):
        """
        Database: ird_db_v1
        Description: abc        
        """
        @classmethod
        def get_db_name(cls):
            return "ird_db_v1"

        @classmethod
        def get_table_name(cls):
            return "campaign_tbl_v2"
    
# --- gen code block ---