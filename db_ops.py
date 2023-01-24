import psycopg
import yaml
from yaml.loader import SafeLoader

class DB_OPS:
    config_file = "./conn_details.yaml"
    def __init__(self):
        # Open the file and load the file
        with open(config_file) as cf:
            self.conn_dict = yaml.load(cf, Loader=SafeLoader)

        self.conn = psycopg.connect(
            "host={} dbname={} user={} password={} port={}".format(
                self.conn_dict["host"],
                self.conn_dict["dbname"],
                self.conn_dict["user"],
                self.conn_dict["password"],
                self.conn_dict["port"],
            )
        )
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
          categoryName TEXT,
          parentCategoryName TEXT NOT NULL,
          FOREIGN KEY (productId) REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
        self.product_table_insert = "INSERT INTO {} ({}, {}, {}, {}, {}, {}, {}) VALUES (%s, %s, %s, %s, %s, %s, %s)".format(
            "product",
            "id",
            "name",
            "title",
            "price",
            "availability",
            "productDescription",
            "productImageUrl",
        )
        self.category_table_insert = (
            "INSERT INTO {} ({}, {}, {}) VALUES (%s, %s, %s)".format(
                "category", "productId", "categoryName", "parentCategoryName"
            )
        )

    def create(self):
        self.conn.execute(self.CATEGORY_TABLE_DROP)
        self.conn.execute(self.PRODUCT_TABLE_DROP)
        self.conn.execute(self.PRODUCT_TABLE_CREATE)
        self.conn.execute(self.CATEGORY_TABLE_CREATE)
        self.conn.commit()

    def insert(self, data):
        product_insert_data = (
            data["uniqueId"],
            data["name"],
            data["title"],
            data["price"],
            data["availability"],
            data.get("productDescription", ""),
            data["productImage"],
        )
        category_insert_data = (
            data["uniqueId"],
            data.get("catlevel2Name", ""),
            data["catlevel1Name"],
        )
        self.conn.execute(product_table_insert, product_insert_data)
        self.conn.execute(category_table_insert, category_insert_data)
        self.conn.commit()
