# --- render code block -----
from databloom._core.postgres_core import PostgresqlBase

class sourceNew(PostgresqlBase):
    def __init__(self, get_credential_from_server) -> None:
        self.id = "67c9718c04f1f10fbe916978"
        self.credential = get_credential_from_server(self.id)
# --- render code block -----
