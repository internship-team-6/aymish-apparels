from cat_level_2_with_parent_id.dao.index import CatLevel2WithParentIdDAO


class CatLevel2WithParentIdService:
    def __init__(self):
        self.dao = CatLevel2WithParentIdDAO()

    def select_cat_level_2_list_with_parent_id(self, cat_level_1_id):
        r_key = "cat-level-2-with-parent-id->{}".format(cat_level_1_id)
        cat_level_2_name_id_list_with_cat_level_1_id = self.dao.cache_ops.get(r_key)
        if cat_level_2_name_id_list_with_cat_level_1_id is None:
            cat_level_2_name_id_list_with_cat_level_1_id = (
                self.dao.select_cat_level_2_name_id_list_with_parent_id(cat_level_1_id)
            )
            self.dao.cache_ops.set(r_key, cat_level_2_name_id_list_with_cat_level_1_id)
        return cat_level_2_name_id_list_with_cat_level_1_id
