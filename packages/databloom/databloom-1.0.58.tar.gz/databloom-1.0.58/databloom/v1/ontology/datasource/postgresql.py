import databloom._dynamic.source.postgresql as db
from typing import Callable

class Postgres:
    """
    data source type is postgresql
    """
    def __init__(self, get_credential_from_sdk: Callable) -> None:
        ## ----render code block-----
        
        self.ABC = db.ABC(get_credential_from_sdk)
        
        self.hainv4testing = db.hainv4testing(get_credential_from_sdk)
        
        self.sourceNew = db.sourceNew(get_credential_from_sdk)
        
        ## ----render code block----
        pass
