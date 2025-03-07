# ---- render code block -----
from databloom._core.dataset import DatasetBase
from .table import *

class hainv4test(DatasetBase):
    def __init__(self) -> None:
        self.database_id = "67c94a2604f1f10fbe916977"
        self.database_name  = "hainv4test"
        
        self.table12 = table12(self.database_name)
        
# ---- render code block 
    
