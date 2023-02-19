from cat_level_1.dao.index import CatLevel1DAO


class CatLevel1Service:
    def __init__(self):
        self.dao = CatLevel1DAO()

    def select_categories(self):
        r_key = "cat-level-1->{}".format("categories")
        categories = self.dao.cache_ops.get(r_key)
        if categories is None:
            categories = self.dao.select_cat_level_1_name_id_list()
            self.dao.cache_ops.set(r_key, categories)
        return categories
