from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class IrdDbV2(DatasetBase):
    """
    Database: IrdDbV2
    Description: testing
   
    """
    def __init__(self):
        pass
        
    
    class Marketingv1(TableBase):
        """
        Database: IrdDbV2
        Description: Marketing        
        """
        @classmethod
        def get_db_name(cls):
            return "irddbv2"

        @classmethod
        def get_table_name(cls):
            return "marketingv1"
    
    class AggByIndustry(TableBase):
        """
        Database: IrdDbV2
        Description: agg by industry        
        """
        @classmethod
        def get_db_name(cls):
            return "irddbv2"

        @classmethod
        def get_table_name(cls):
            return "aggbyindustry"
    
# --- gen code block ---