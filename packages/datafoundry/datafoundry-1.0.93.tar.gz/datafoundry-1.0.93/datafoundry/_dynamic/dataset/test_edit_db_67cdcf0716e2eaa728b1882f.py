from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class test_edit_db(DatasetBase):
    """
    Database: test_edit_db
    Description: None
   
    """
    def __init__(self):
        pass
        
    
    class test_edit_table(TableBase):
        """
        Database: test_edit_db
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "test_edit_db"

        @classmethod
        def get_table_name(cls):
            return "test_edit_table"
    
# --- gen code block ---