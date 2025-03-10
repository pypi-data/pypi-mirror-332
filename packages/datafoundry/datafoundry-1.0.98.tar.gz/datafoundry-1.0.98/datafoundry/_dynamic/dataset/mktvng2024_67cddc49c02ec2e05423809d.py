from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class mktvng2024(DatasetBase):
    """
    Database: mktvng2024
    Description: mkt vng 2024
   
    """
    def __init__(self):
        pass
        
    
    class pipelineusedata(TableBase):
        """
        Database: mktvng2024
        Description: pipeline use data        
        """
        @classmethod
        def get_db_name(cls):
            return "mktvng2024"

        @classmethod
        def get_table_name(cls):
            return "pipelineusedata"
    
    class usedatapl(TableBase):
        """
        Database: mktvng2024
        Description: usedatapl        
        """
        @classmethod
        def get_db_name(cls):
            return "mktvng2024"

        @classmethod
        def get_table_name(cls):
            return "usedatapl"
    
# --- gen code block ---