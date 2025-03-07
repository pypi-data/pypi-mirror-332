# --- render code block -----
from databloom._core.postgres_core import PostgresqlBase

class HR report(PostgresqlBase):
    def __init__(self, get_credential_from_server) -> None:
        self.id = "67c7cfb9535b6a2668124ff8"
        self.credential = get_credential_from_server(self.id)
# --- render code block -----
