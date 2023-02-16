from category_product_list.dao.index import DAO


class Service:
    def __init__(self):
        self.dao = DAO()

    def select_product_list(self, cat_level_2_id, sort_order=""):
        r_key = "category-product-list->{}".format(cat_level_2_id)
        if sort_order in ("asc", "desc"):
            r_key += "->{}".format(sort_order)
        product_list = self.dao.cache_ops.get(r_key)
        if product_list is None:
            if sort_order == "asc":
                product_list = (
                    self.dao.select_product_list_with_cat_level_2_id_price_asc(
                        cat_level_2_id
                    )
                )
            elif sort_order == "desc":
                product_list = (
                    self.dao.select_product_list_with_cat_level_2_id_price_desc(
                        cat_level_2_id
                    )
                )
            else:
                product_list = self.dao.select_product_list_with_cat_level_2_id(
                    cat_level_2_id
                )
            self.dao.cache_ops.set(r_key, product_list)
        return product_list
