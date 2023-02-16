from common.dao.db_auth import DB_Auth
from common.dao.cache_ops import Cache_Ops


class DAO:
    def __init__(self):
        self.db_auth = DB_Auth()
        self.cache_ops = Cache_Ops()
        self.product_details_from_id_select = """
            SELECT * FROM product
            WHERE id = %s
        """

    def select_product_details_from_id(self, product_id):
        product_details_from_id = self.db_auth.conn.execute(
            self.product_details_from_id_select, (product_id,)
        ).fetchone()
        return product_details_from_id
