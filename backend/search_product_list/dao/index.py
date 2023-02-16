from common.dao.db_auth import DB_Auth


class DAO:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.category_table_insert = """
            INSERT INTO category (name, level, parentid)
            VALUES (%s, %s, %s)
        """
        self.product_table_insert = """
            INSERT INTO product (id, name, title, image, price, description, availability, categoryId)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.latest_cat_id_select = """
            SELECT MAX(id)
            FROM category
        """
        self.cat_level_n_id_from_name_select = """
            SELECT id
            FROM category
            WHERE (
                level = %s
                AND
                name = %s
            )
        """
        self.product_id_list_select = """
            SELECT id
            FROM product
        """

    def select_product_id_list(self):
        product_id_list = list(
            map(
                lambda x: x["id"],
                self.db_auth.conn.execute(self.product_id_list_select).fetchall(),
            )
        )
        return product_id_list

    def select_cat_level_n_id_from_name(self, level, name):
        cat_level_n_id_from_name = self.db_auth.conn.execute(
            self.cat_level_n_id_from_name_select, (level, name)
        ).fetchone()
        if cat_level_n_id_from_name is not None:
            return cat_level_n_id_from_name["id"]
        return None

    def select_latest_cat_id(self):
        latest_cat_id = self.db_auth.conn.execute(self.latest_cat_id_select).fetchone()
        if latest_cat_id is not None:
            return latest_cat_id["max"]
        return None

    def insert_category_table(self, name, level, parent_id=None):
        params = [name, level]
        if parent_id:
            params.append(parent_id)
        params = tuple(params)
        self.db_auth.conn.execute(self.category_table_insert, (name, level, parent_id))
        self.db_auth.conn.commit()
        return True

    def insert_product_table(
        self,
        product_id,
        name,
        title,
        image,
        price,
        description,
        availability,
        category_id,
    ):
        self.db_auth.conn.execute(
            self.product_table_insert,
            (
                product_id,
                name,
                title,
                image,
                price,
                description,
                availability,
                category_id,
            ),
        )
        self.db_auth.conn.commit()
        return True

    def insert(
        self,
        product_id,
        name,
        title,
        image,
        price,
        description,
        availability,
        cat_level_1_name,
        cat_level_2_name,
    ):
        product_id_list = self.select_product_id_list()
        if product_id in product_id_list:
            return False
        cat_level_1_id = self.select_cat_level_n_id_from_name(1, cat_level_1_name)
        if cat_level_1_id is None:
            self.insert_category_table(cat_level_1_name, 1, None)
            cat_level_1_id = self.select_latest_cat_id()
        cat_level_2_id = self.select_cat_level_n_id_from_name(2, cat_level_2_name)
        if cat_level_2_id is None:
            self.insert_category_table(cat_level_2_name, 2, cat_level_1_id)
            cat_level_2_id = self.select_latest_cat_id()
        self.insert_product_table(
            product_id,
            name,
            title,
            image,
            price,
            description,
            availability,
            cat_level_2_id,
        )
        return True
