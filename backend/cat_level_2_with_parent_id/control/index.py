from flask import request
from flask_restful import Resource
from cat_level_2_with_parent_id.service.index import CatLevel2WithParentIdService


class CatLevel2WithParentIdControl(Resource):
    def __init__(self):
        self.service = CatLevel2WithParentIdService()

    def get(self):
        # obtain parameters
        cat_level_1_id = request.args.get("catlevel1Id")
        
        # get list of categories having level 2 given parent id
        cat_level_2_list = self.service.select_cat_level_2_list_with_parent_id(
            cat_level_1_id
        )
        return cat_level_2_list
