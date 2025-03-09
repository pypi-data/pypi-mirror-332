from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class gamemetric(DatasetBase):
    """
    Database: gamemetric
    Description: Game analyze data warehouse
   
    """
    def __init__(self):
        pass
        
    
    class catmetrics(TableBase):
        """
        Database: gamemetric
        Description: Cate table        
        """
        @classmethod
        def get_db_name(cls):
            return "gamemetric"

        @classmethod
        def get_table_name(cls):
            return "catmetrics"
    
# --- gen code block ---