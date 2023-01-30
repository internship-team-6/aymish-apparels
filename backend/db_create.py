from db_auth import DB_Auth


class DB_Create:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.conn = self.db_auth.conn
        self.CATEGORY_TABLE_DROP = "DROP TABLE IF EXISTS category"
        self.PRODUCT_TABLE_DROP = "DROP TABLE IF EXISTS product"
        self.PRODUCT_TABLE_CREATE = """
        CREATE TABLE product
        (
          id TEXT NOT NULL,
          name TEXT NOT NULL,
          title TEXT NOT NULL,
          price FLOAT NOT NULL,
          availability BOOLEAN NOT NULL,
          productDescription TEXT,
          productImageUrl TEXT NOT NULL,
          PRIMARY KEY (id)
        );
        """
        self.CATEGORY_TABLE_CREATE = """
        CREATE TABLE category
        (
          productId TEXT NOT NULL,
          catlevel2Name TEXT,
          catlevel1Name TEXT NOT NULL,
          FOREIGN KEY (productId) REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """

    def create(self):
        self.conn.execute(self.CATEGORY_TABLE_DROP)
        self.conn.execute(self.PRODUCT_TABLE_DROP)
        self.conn.execute(self.PRODUCT_TABLE_CREATE)
        self.conn.execute(self.CATEGORY_TABLE_CREATE)
        self.conn.commit()


db_create = DB_Create()
db_create.create()
print("db created")
