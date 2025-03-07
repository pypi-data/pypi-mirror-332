# --- render code block -----
from databloom._core.postgres_core import PostgresqlBase

class ABC(PostgresqlBase):
    def __init__(self, get_credential_from_server) -> None:
        self.id = "67c80335535b6a2668124ffb"
        self.credential = get_credential_from_server(self.id)
# --- render code block -----
