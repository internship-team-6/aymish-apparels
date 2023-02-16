from pathlib import Path
from sys import path as sys_path

sys_path.insert(0, str(Path(".").absolute()) + "/common/dao")
from common.dao.db_auth import DB_Auth
from common.dao.cache_ops import Cache_Ops


class DAO:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.cache_ops = Cache_Ops()
        self.limit = 15
        self.product_list_with_cat_level_2_id_select = """
            SELECT id, title, image, price
            FROM product
            WHERE categoryId = %s
            LIMIT {}
            OFFSET %s
        """.format(
            self.limit
        )
        self.product_list_with_cat_level_2_id_price_asc_select = """
            SELECT id, title, image, price
            FROM product
            WHERE categoryId = %s
            ORDER BY price ASC
            LIMIT {}
            OFFSET %s
        """.format(
            self.limit
        )
        self.product_list_with_cat_level_2_id_price_desc_select = """
            SELECT id, title, image, price
            FROM product
            WHERE categoryId = %s
            ORDER BY price DESC
            LIMIT {}
            OFFSET %s
        """.format(
            self.limit
        )

    def get_limit(self):
        return self.limit

    def select_product_list_with_cat_level_2_id(self, category_id, offset):
        product_list_with_cat_level_2_id = self.db_auth.conn.execute(
            self.product_list_with_cat_level_2_id_select, (category_id, offset)
        ).fetchall()
        return product_list_with_cat_level_2_id

    def select_product_list_with_cat_level_2_id_price_asc(self, category_id, offset):
        product_list_with_cat_level_2_id_price_asc = self.db_auth.conn.execute(
            self.product_list_with_cat_level_2_id_price_asc_select,
            (category_id, offset),
        ).fetchall()
        return product_list_with_cat_level_2_id_price_asc

    def select_product_list_with_cat_level_2_id_price_desc(self, category_id, offset):
        offset = (page - 1) * limit
        product_list_with_cat_level_2_id_price_desc = self.db_auth.conn.execute(
            self.product_list_with_cat_level_2_id_price_desc_select,
            (category_id, offset),
        ).fetchall()
        return product_list_with_cat_level_2_id_price_desc
