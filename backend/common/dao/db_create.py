from common.dao.db_auth import DB_Auth


class DB_Create:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.category_table_if_not_exists_create = """
            CREATE TABLE IF NOT EXISTS category (
                id SERIAL NOT NULL,
                name TEXT NOT NULL,
                level INT NOT NULL,
                parentId INT,
                PRIMARY KEY (id)
            )
            """
        self.product_table_if_not_exists_create = """
            CREATE TABLE IF NOT EXISTS product (
                id TEXT NOT NULL,
                name TEXT NOT NULL,
                title TEXT NOT NULL,
                image TEXT NOT NULL,
                price FLOAT NOT NULL,
                description TEXT,
                availability BOOLEAN NOT NULL,
                categoryId INT NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (categoryId) REFERENCES category(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
            )
        """

    def create_category_table_if_not_exists(self):
        self.db_auth.conn.execute(self.category_table_if_not_exists_create)
        self.db_auth.conn.commit()

    def create_product_table_if_not_exists(self):
        self.db_auth.conn.execute(self.product_table_if_not_exists_create)
        self.db_auth.conn.commit()
