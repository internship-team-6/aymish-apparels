from navbar.dao.index import DAO


class Service:
    def __init__(self):
        self.dao = DAO()

    def select_categories(self):
        r_key = "navbar->{}".format("categories")
        categories = self.dao.cache_ops.get(r_key)
        if categories is None:
            categories = self.dao.select_cat_level_1_name_id_list()
            self.dao.cache_ops.set(r_key, categories)
        return categories
