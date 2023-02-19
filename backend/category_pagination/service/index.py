from category_pagination.dao.index import CategoryPaginationDAO


class CategoryPaginationService:
    def __init__(self):
        self.dao = CategoryPaginationDAO()
        self.limit = 15

    def pages_count(self, cat_level_2_id):
        count_product_list_with_cat_level_2_id = (
            self.dao.select_count_product_list_with_cat_level_2_id(cat_level_2_id)[
                "count"
            ]
        )
        no_pages = count_product_list_with_cat_level_2_id // self.limit + (
            count_product_list_with_cat_level_2_id % self.limit and 1
        )
        return no_pages
