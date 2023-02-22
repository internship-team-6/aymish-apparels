from category_pagination.dao.index import CategoryPaginationDAO


class CategoryPaginationService:
    def __init__(self):
        self.dao = CategoryPaginationDAO()
        
        # no. of items per page
        self.limit = 15

    def pages_count(self, cat_level_2_id):
        count_product_list_with_cat_level_2_id = (
            self.dao.select_count_product_list_with_cat_level_2_id(cat_level_2_id)[
                "count"
            ]
        )
        # logic for calculating total no. of pages given no. of items
        no_pages = count_product_list_with_cat_level_2_id // self.limit + (
            count_product_list_with_cat_level_2_id % self.limit and 1
        )
        return no_pages
