from category_product_list.dao.index import CategoryProductListDAO


class CategoryProductListService:
    def __init__(self):
        self.dao = CategoryProductListDAO()

    def select_product_list(self, cat_level_2_id, sort_order, page):
        r_key = "category-product-list->{}->{}".format(cat_level_2_id, page)
        if sort_order in ("asc", "desc"):
            r_key += "->{}".format(sort_order)
        product_list = self.dao.cache_ops.get(r_key)
        if product_list is None:
            # logic for calculating offset (i.e. no. of items to be skipped from the beginning)
            offset = (page - 1) * self.dao.get_limit()

            if sort_order == "asc":
                product_list = (
                    self.dao.select_product_list_with_cat_level_2_id_price_asc(
                        cat_level_2_id, offset
                    )
                )
            elif sort_order == "desc":
                product_list = (
                    self.dao.select_product_list_with_cat_level_2_id_price_desc(
                        cat_level_2_id, offset
                    )
                )
            else:
                product_list = self.dao.select_product_list_with_cat_level_2_id(
                    cat_level_2_id, offset
                )
            self.dao.cache_ops.set(r_key, product_list)
        return product_list
