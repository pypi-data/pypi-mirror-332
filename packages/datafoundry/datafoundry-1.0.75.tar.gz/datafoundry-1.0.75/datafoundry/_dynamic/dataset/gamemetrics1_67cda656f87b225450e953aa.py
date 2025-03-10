from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class gamemetrics1(DatasetBase):
    """
    Database: gamemetrics1
    Description: gamemetrics1
   
    """
    def __init__(self):
        pass
        
    
    class pipelineanalysis(TableBase):
        """
        Database: gamemetrics1
        Description: pipeline analysis        
        """
        @classmethod
        def get_db_name(cls):
            return "gamemetrics1"

        @classmethod
        def get_table_name(cls):
            return "pipelineanalysis"
    
# --- gen code block ---