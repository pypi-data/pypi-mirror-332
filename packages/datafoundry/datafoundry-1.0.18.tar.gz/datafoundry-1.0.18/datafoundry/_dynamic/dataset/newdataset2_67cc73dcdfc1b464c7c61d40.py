from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class NewDataset2(DatasetBase):
    """
    Database: NewDataset2
    Description: None
   
    """
    def __init__(self):
        pass
        
    
    class NewTable1(TableBase):
        """
        Database: NewDataset2
        Description: asdvad sdv asdvasdv        
        """
        @classmethod
        def get_db_name(cls):
            return "NewDataset2"

        @classmethod
        def get_table_name(cls):
            return "NewTable1"
    
# --- gen code block ---