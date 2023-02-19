from product.dao.index import ProductDAO


class ProductService:
    def __init__(self):
        self.dao = ProductDAO()

    def select_product(self, product_id):
        r_key = "product->{}".format(product_id)
        product_details = self.dao.cache_ops.get(r_key)
        if product_details is None:
            product_details = self.dao.select_product_details_from_id(product_id)
            self.dao.cache_ops.set(r_key, product_details)
        return product_details
