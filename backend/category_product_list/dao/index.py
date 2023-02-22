from pathlib import Path
from sys import path as sys_path

sys_path.insert(0, str(Path(".").absolute()) + "/common/dao")
from common.dao.db_auth import DB_Auth
from common.dao.cache_ops import Cache_Ops


class CategoryProductListDAO:
    def __init__(self):
        # object for performing operations on database
        self.db_auth = DB_Auth()

        # object for performing operations on cache
        self.cache_ops = Cache_Ops()
        
        # no. of products to be displayed per page
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

    # get list of products belonging to the given category id
    def select_product_list_with_cat_level_2_id(self, category_id, offset):
        product_list_with_cat_level_2_id = self.db_auth.conn.execute(
            self.product_list_with_cat_level_2_id_select, (category_id, offset)
        ).fetchall()
        return product_list_with_cat_level_2_id

    # get list of products belonging to the given category id sorted in ascending order
    def select_product_list_with_cat_level_2_id_price_asc(self, category_id, offset):
        product_list_with_cat_level_2_id_price_asc = self.db_auth.conn.execute(
            self.product_list_with_cat_level_2_id_price_asc_select,
            (category_id, offset),
        ).fetchall()
        return product_list_with_cat_level_2_id_price_asc

    # get list of products belonging to the given category id sorted in descending order
    def select_product_list_with_cat_level_2_id_price_desc(self, category_id, offset):
        product_list_with_cat_level_2_id_price_desc = self.db_auth.conn.execute(
            self.product_list_with_cat_level_2_id_price_desc_select,
            (category_id, offset),
        ).fetchall()
        return product_list_with_cat_level_2_id_price_desc
