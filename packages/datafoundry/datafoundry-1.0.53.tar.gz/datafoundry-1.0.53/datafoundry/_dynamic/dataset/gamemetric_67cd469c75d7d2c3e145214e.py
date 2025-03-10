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
    
    class statustable(TableBase):
        """
        Database: gamemetric
        Description:         
        """
        @classmethod
        def get_db_name(cls):
            return "gamemetric"

        @classmethod
        def get_table_name(cls):
            return "statustable"
    
    class gamedata(TableBase):
        """
        Database: gamemetric
        Description: game data        
        """
        @classmethod
        def get_db_name(cls):
            return "gamemetric"

        @classmethod
        def get_table_name(cls):
            return "gamedata"
    
    class gamedataw(TableBase):
        """
        Database: gamemetric
        Description: Game data        
        """
        @classmethod
        def get_db_name(cls):
            return "gamemetric"

        @classmethod
        def get_table_name(cls):
            return "gamedataw"
    
# --- gen code block ---