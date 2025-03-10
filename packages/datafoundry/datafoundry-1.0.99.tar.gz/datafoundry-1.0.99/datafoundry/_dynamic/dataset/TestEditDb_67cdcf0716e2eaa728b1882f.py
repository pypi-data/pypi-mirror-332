from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class TestEditDb(DatasetBase):
    """
    Database: TestEditDb
    Description: None
   
    """
    def __init__(self):
        pass
        
    
    class TestEditTable(TableBase):
        """
        Database: TestEditDb
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "TestEditDb"

        @classmethod
        def get_table_name(cls):
            return "TestEditTable"
    
# --- gen code block ---