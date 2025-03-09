# from ._core import datasource
from ._dynamic import dataset

from .ontology import *
# from ._core import * # for build source
# from ._dynamic import * # for build source
from ._core.version_core import check_for_updates

__version__ = "1.0.8"

__all__ = [
    "Datasource",
    "Dataset",
]

@check_for_updates
def check_for_updates_init():
    print("Checking for updates...")
    pass

__check_for_updates_init = check_for_updates_init()