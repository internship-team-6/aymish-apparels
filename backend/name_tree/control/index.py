from flask_restful import Resource
from flask import request
from name_tree.service.index import NameTreeService


class NameTreeControl(Resource):
    def __init__(self):
        self.service = NameTreeService()

    def get(self):
        # obtain parameters
        cat_level_2_id = request.args.get("catlevel2Id")
        
        # get list of names for categories in bottom up manner given category id
        name_list = self.service.select_name_tree(cat_level_2_id)
        return name_list
