import databloom._dynamic.dataset as ds
from typing import Callable

class Dataset:
    """
    data source type is mysql
    """
    def __init__(self) -> None:
        ## ----render code block-----
        
        self.hainv4test = ds.hainv4test()
        self.abc = ds.abc()
        ## ----render code block----
        pass
