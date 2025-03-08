
from datafoundry._core.dataset import DatasetBase
from datafoundry._core.dataset.table_core import TableBase


# --- gen code block ---
class hainv4(DatasetBase):
    """
    TODO: cron generate DB description
    """
    def __init__(self):
        pass
        
    class table1(TableBase):
        @classmethod
        def get_db_name(cls):
            # TODO: cron generate DB hainv4 description
            # TODO: cron generate db hainv4 name
            return "public"

        @classmethod
        def get_table_name(cls):
            # TODO: cron generate table description
            # TODO: cron generate table name
            return "table1"
    
    class table2(TableBase):
        @classmethod
        def init_table(cls):
            # TODO: cron generate DB description
            # TODO: cron generate db name
            print("table_2")
    
# --- gen code block ---