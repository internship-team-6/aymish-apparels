from flask import request
from flask_restful import Resource
from dropdown.service.index import Service


class DropDownControl(Resource):
    def __init__(self):
        self.service = Service()

    def get(self):
        cat_level_1_id = request.args.get("catlevel1Id")
        cat_level_2_list = self.service.select_cat_level_2_list_with_parent_id(
            cat_level_1_id
        )
        return cat_level_2_list
