from dropdown.dao.index import DAO


class Service:
    def __init__(self):
        self.dao = DAO()

    def select_cat_level_2_list_with_parent_id(self, cat_level_1_id):
        r_key = "dropdown->{}".format(cat_level_1_id)
        cat_level_2_name_id_list_with_cat_level_1_id = self.dao.cache_ops.get(r_key)
        if cat_level_2_name_id_list_with_cat_level_1_id is None:
            cat_level_2_name_id_list_with_cat_level_1_id = (
                self.dao.select_cat_level_2_name_id_list_with_parent_id(cat_level_1_id)
            )
            self.dao.cache_ops.set(r_key, cat_level_2_name_id_list_with_cat_level_1_id)
        return cat_level_2_name_id_list_with_cat_level_1_id
