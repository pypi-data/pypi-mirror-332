# --- render code block -----
from databloom._core.postgres_core import PostgresqlBase

class hainv4testing(PostgresqlBase):
    def __init__(self, get_credential_from_server) -> None:
        self.id = "67c8063e535b6a2668124ffd"
        self.credential = get_credential_from_server(self.id)
# --- render code block -----
