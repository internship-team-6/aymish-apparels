from common.dao.cache_ops import Cache_Ops
from common.dao.db_auth import DB_Auth

class DAO:
    def __init__(self):
        self.cache_ops=Cache_Ops()
        self.db_auth=DB_Auth()
        self.product_details_from_id_select = """
            SELECT id, name, image, price, description
            FROM product
            WHERE id = %s
        """
        self.id_name_list_from_products_select = """
            SELECT id, name
            FROM product
        """

    def select_product_details_from_id(self, product_id):
        product_details_from_id=self.db_auth.conn.execute(self.product_details_from_id_select, (product_id,)).fetchone()
        return product_details_from_id

    def select_id_name_list_from_products(self):
        id_name_list_from_products = self.db_auth.conn.execute(self.id_name_list_from_products_select).fetchall()
        return id_name_list_from_products
