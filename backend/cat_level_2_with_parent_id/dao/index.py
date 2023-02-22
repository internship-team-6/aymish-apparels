from common.dao.db_auth import DB_Auth
from common.dao.cache_ops import Cache_Ops


class CatLevel2WithParentIdDAO:
    def __init__(self):
        # object for performing operations on database
        self.db_auth = DB_Auth()

        # object for performing operations on cache
        self.cache_ops = Cache_Ops()

        self.cat_level_2_name_id_list_with_parent_id_select = """
            SELECT id, name
            FROM category
            WHERE parentId = %s
        """

    def select_cat_level_2_name_id_list_with_parent_id(self, parent_id):
        cat_level_2_name_id_list_with_parent_id = self.db_auth.conn.execute(
            self.cat_level_2_name_id_list_with_parent_id_select,
            (parent_id,),
        ).fetchall()
        return cat_level_2_name_id_list_with_parent_id
