from db_auth import DB_Auth


class DB_Ops:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.conn = self.db_auth.conn
        id_select_statement = "SELECT {} FROM {}".format("id", "product")
        self.product_table_select = "SELECT {} FROM {}".format("*", "product")
        self.category_table_select = "SELECT {} FROM {}".format("*", "category")
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
                "category", "productId", "catlevel2Name", "catlevel1Name"
            )
        )
        self.product_table_update = "UPDATE {} SET ({}, {}, {}, {}, {}, {}) = (%s, %s, %s, %s, %s, %s) WHERE {} = %s".format(
            "product",
            "name",
            "title",
            "price",
            "availability",
            "productDescription",
            "productImageUrl",
            "id",
        )
        self.category_table_update = (
            "UPDATE {} SET ({}, {}) = (%s, %s) WHERE {} = %s".format(
                "category", "catlevel2Name", "catlevel1Name", "productId"
            )
        )
        self.product_table_delete = "DELETE FROM {} WHERE {} = %s".format(
            "product", "id"
        )
        self.category_table_delete = "DELETE FROM {} WHERE {} = %s".format(
            "category", "productId"
        )
        self.id_set = set(
            map(lambda x: x[0], self.conn.execute(id_select_statement).fetchall())
        )

    def id_exists(self, unique_id):
        return unique_id in self.id_set

    def select_products(self):
        product_select_data = self.conn.execute(self.product_table_select).fetchall()[
            :5
        ]
        return product_select_data

    def select_categories(self):
        category_select_data = self.conn.execute(self.category_table_select).fetchall()[
            :5
        ]
        return category_select_data

    def insert(self, data):
        unique_id = data["uniqueId"]
        if self.id_exists(unique_id):
            return False
        product_insert_data = (
            unique_id,
            data["name"],
            data["title"],
            data["price"],
            data["availability"],
            data.get("productDescription", ""),
            data["productImage"],
        )
        category_insert_data = (
            unique_id,
            data.get("catlevel2Name", ""),
            data["catlevel1Name"],
        )
        self.conn.execute(self.product_table_insert, product_insert_data)
        self.conn.execute(self.category_table_insert, category_insert_data)
        self.conn.commit()
        self.id_set.add(unique_id)
        return True

    def update(self, data):
        unique_id = data["uniqueId"]
        if not self.id_exists(unique_id):
            return self.insert(data)
        product_update_data = (
            data["name"],
            data["title"],
            data["price"],
            data["availability"],
            data.get("productDescription", ""),
            data["productImage"],
            unique_id,
        )
        category_update_data = (
            data.get("catlevel2Name", ""),
            data["catlevel1Name"],
            unique_id,
        )
        self.conn.execute(product_table_update, product_update_data)
        self.conn.execute(category_table_update, category_update_data)
        self.conn.commit()
        return True

    def delete(self, unique_id):
        if not self.id_exists(unique_id):
            return False
        self.conn.execute(product_table_delete, uniqueId)
        self.conn.execute(category_table_delete, uniqueId)
        self.conn.commit()
        self.id_set.remove(unique_id)
        return True
