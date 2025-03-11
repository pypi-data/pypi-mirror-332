from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class Mktvng2024(DatasetBase):
    """
    Database: Mktvng2024
    Description: mkt vng 2024
   
    """
    def __init__(self):
        pass
        
    
    class Pipelineusedata(TableBase):
        """
        Database: Mktvng2024
        Description: pipeline use data        
        """
        @classmethod
        def get_db_name(cls):
            return "mktvng2024"

        @classmethod
        def get_table_name(cls):
            return "pipelineusedata"
    
    class Usedatapl(TableBase):
        """
        Database: Mktvng2024
        Description: usedatapl        
        """
        @classmethod
        def get_db_name(cls):
            return "mktvng2024"

        @classmethod
        def get_table_name(cls):
            return "usedatapl"
    
    class ActualRawData(TableBase):
        """
        Database: Mktvng2024
        Description: actual_raw_data        
        """
        @classmethod
        def get_db_name(cls):
            return "mktvng2024"

        @classmethod
        def get_table_name(cls):
            return "actualrawdata"
    
# --- gen code block ---