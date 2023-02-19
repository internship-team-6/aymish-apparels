from pathlib import Path
from sys import path as sys_path

sys_path.insert(0, str(Path(".").absolute()) + "/common/dao")

from common.dao.cache_ops import Cache_Ops
from common.dao.db_auth import DB_Auth


class NameTreeDAO:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.cache_ops = Cache_Ops()
        self.category_name_from_id_select = """
            SELECT name
            FROM category
            WHERE id = %s
        """
        self.parent_id_name_from_id_select = """
            SELECT name, id
            FROM category
            WHERE id in (
                SELECT parentId
                FROM category
                WHERE (
                    id = %s
                    AND
                    parentId IS NOT NULL
                )
            )
        """

    def select_category_name_from_id(self, category_id):
        category_name_from_id = self.db_auth.conn.execute(
            self.category_name_from_id_select, (category_id,)
        ).fetchone()
        return category_name_from_id

    def select_parent_id_name_from_id(self, category_id):
        parent_id_name_from_id = self.db_auth.conn.execute(
            self.parent_id_name_from_id_select, (category_id,)
        ).fetchone()
        return parent_id_name_from_id
