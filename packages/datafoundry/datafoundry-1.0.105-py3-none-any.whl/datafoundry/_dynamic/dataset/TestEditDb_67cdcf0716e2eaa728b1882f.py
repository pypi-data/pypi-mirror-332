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
            return "testeditdb"

        @classmethod
        def get_table_name(cls):
            return "testedittable"
    
    class Tabletest(TableBase):
        """
        Database: TestEditDb
        Description: abc        
        """
        @classmethod
        def get_db_name(cls):
            return "testeditdb"

        @classmethod
        def get_table_name(cls):
            return "tabletest"
    
    class Abc(TableBase):
        """
        Database: TestEditDb
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "testeditdb"

        @classmethod
        def get_table_name(cls):
            return "abc"
    
    class Table10(TableBase):
        """
        Database: TestEditDb
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "testeditdb"

        @classmethod
        def get_table_name(cls):
            return "table10"
    
# --- gen code block ---