from name_tree.service.index import Service
from flask_restful import Resource
from flask import request


class NameTreeControl(Resource):
    def __init__(self):
        self.service = Service()

    def get(self):
        cat_level_2_id = request.args.get("catlevel2Id")
        name_list = self.service.select_name_tree(cat_level_2_id)
        return name_list
