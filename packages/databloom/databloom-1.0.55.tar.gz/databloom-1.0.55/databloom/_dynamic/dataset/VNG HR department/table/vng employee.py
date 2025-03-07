# ---- render code block -----
from databloom._core.dataset.table_core import TableBase

class vng employee(TableBase):
    """
    employees having contract with vng
    """
    def __init__(self, db_name: str) -> None:
        self.table_id = "2ed7bcc9-f567-4349-8de2-ae1993aa7583"
        self.table_name = "vng employee"
        self.set_db_name(db_name)
# ---- render code block -----
