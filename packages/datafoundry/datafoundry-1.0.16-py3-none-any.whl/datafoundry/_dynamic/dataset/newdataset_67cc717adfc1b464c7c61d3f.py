from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class NewDataset(DatasetBase):
    """
    Database: NewDataset
    Description: None
   
    """
    def __init__(self):
        pass
        
    
    class NewTable(TableBase):
        """
        Database: NewDataset
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "NewDataset"

        @classmethod
        def get_table_name(cls):
            return "NewTable"
    
    class another_table(TableBase):
        """
        Database: NewDataset
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "NewDataset"

        @classmethod
        def get_table_name(cls):
            return "another_table"
    
    class another_table_2(TableBase):
        """
        Database: NewDataset
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "NewDataset"

        @classmethod
        def get_table_name(cls):
            return "another_table_2"
    
# --- gen code block ---