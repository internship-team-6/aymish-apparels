from name_tree.dao.index import NameTreeDAO


class NameTreeService:
    def __init__(self):
        self.dao = NameTreeDAO()

    def select_name_tree(self, cat_id):
        r_key = "name-tree->{}".format(cat_id)
        name_list = self.dao.cache_ops.get(r_key)
        
        # get list of names in from bottom to top in order of level
        if name_list is None:
            name_list = []
            cat_name = self.dao.select_category_name_from_id(cat_id)["name"]
            name_list.append(cat_name)
            cat_id_name = self.dao.select_parent_id_name_from_id(cat_id)
            while cat_id_name:
                cat_id, cat_name = cat_id_name["id"], cat_id_name["name"]
                name_list.append(cat_name)
                cat_id_name = self.dao.select_parent_id_name_from_id(cat_id)

            # reverse the list of values since we want to display category names from left to right in ascending order of levels
            name_list = name_list[::-1]
            self.dao.cache_ops.set(r_key, name_list)
        return name_list
