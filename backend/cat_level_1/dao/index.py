from common.dao.db_auth import DB_Auth
from common.dao.cache_ops import Cache_Ops


class CatLevel1DAO:
    def __init__(self):
        # object for performing operations on database
        self.db_auth = DB_Auth()
        
        # object for performing operations on cache
        self.cache_ops = Cache_Ops()

        self.cat_level_1_name_id_list_select = """
            SELECT name, id
            FROM category
            WHERE level = 1
        """

    def select_cat_level_1_name_id_list(self):
        cat_level_1_name_id_list = self.db_auth.conn.execute(
            self.cat_level_1_name_id_list_select
        ).fetchall()
        return cat_level_1_name_id_list
