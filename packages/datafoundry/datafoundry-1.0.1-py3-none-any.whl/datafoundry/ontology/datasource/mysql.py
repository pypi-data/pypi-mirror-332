import datafoundry._dynamic.source.mysql as db
from typing import Callable

## ----render code block-----
class Mysql:
    """
    data source type is mysql
    """
    def __init__(self, get_credential_from_sdk: Callable) -> None:
        pass
        
## ----render code block----