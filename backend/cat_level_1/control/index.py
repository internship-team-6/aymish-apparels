from flask_restful import Resource
from cat_level_1.service.index import CatLevel1Service


class CatLevel1Control(Resource):
    def __init__(self):
        self.service = CatLevel1Service()

    def get(self):
        categories = self.service.select_categories()
        return categories
