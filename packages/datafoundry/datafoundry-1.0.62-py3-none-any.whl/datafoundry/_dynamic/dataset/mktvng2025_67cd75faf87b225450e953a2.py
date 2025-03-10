from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class mktvng2025(DatasetBase):
    """
    Database: mktvng2025
    Description: mkt vng 2025
   
    """
    def __init__(self):
        pass
        
    
    class pipelinerawdata(TableBase):
        """
        Database: mktvng2025
        Description: pipeline analysis        
        """
        @classmethod
        def get_db_name(cls):
            return "mktvng2025"

        @classmethod
        def get_table_name(cls):
            return "pipelinerawdata"
    
# --- gen code block ---