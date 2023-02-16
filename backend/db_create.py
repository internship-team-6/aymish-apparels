from db_auth import DB_Auth
from db_statements import DB_Statements


class DB_Create:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.db_statements = DB_Statements()
        self.db_auth.conn.execute(self.db_statements.PRODUCT_TABLE_IF_NOT_EXISTS_CREATE)
        self.db_auth.conn.execute(
            self.db_statements.CATEGORY_TABLE_IF_NOT_EXISTS_CREATE
        )
        self.db_auth.conn.commit()
