from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class Datasettest(DatasetBase):
    """
    Database: Datasettest
    Description: lorem ipsum promax
   
    """
    def __init__(self):
        pass
        
    
    class tabular_3(TableBase):
        """
        Database: Datasettest
        Description: lorem ipsum 111        
        """
        @classmethod
        def get_db_name(cls):
            return "Datasettest"

        @classmethod
        def get_table_name(cls):
            return "tabular_3"
    
# --- gen code block ---