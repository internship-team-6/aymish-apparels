from db_auth import DB_Auth
from db_statements import DB_Statements


class DB_Create:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.db_statements = DB_Statements()

    def create(self):
        self.db_auth.conn.execute(self.db_statements.CATEGORY_TABLE_DROP)
        self.db_auth.conn.execute(self.db_statements.PRODUCT_TABLE_DROP)
        self.db_auth.conn.execute(self.db_statements.PRODUCT_TABLE_CREATE)
        self.db_auth.conn.execute(self.db_statements.CATEGORY_TABLE_CREATE)
        self.db_auth.conn.commit()


db_create = DB_Create()
db_create.create()
print("db created")
