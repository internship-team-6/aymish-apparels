from pathlib import Path
from sys import path as sys_path

sys_path.insert(0, str(Path(".").absolute()) + "/common/dao")
from common.dao.db_auth import DB_Auth
from common.dao.cache_ops import Cache_Ops


class CategoryPaginationDAO:
    def __init__(self):
        # object for performing operations on database
        self.db_auth = DB_Auth()

        # object for performing operations on cache
        self.cache_ops = Cache_Ops()
        self.count_product_list_with_cat_level_2_id_select = """
            SELECT COUNT(*)
            FROM product
            WHERE categoryId = %s
        """

    def select_count_product_list_with_cat_level_2_id(self, category_id):
        count_product_list_with_cat_level_2_id = self.db_auth.conn.execute(
            self.count_product_list_with_cat_level_2_id_select, (category_id,)
        ).fetchone()
        return count_product_list_with_cat_level_2_id
