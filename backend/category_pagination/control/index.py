from flask import request
from flask_restful import Resource
from category_pagination.service.index import CategoryPaginationService


class CategoryPaginationControl(Resource):
    def __init__(self):
        self.service = CategoryPaginationService()

    def get(self):
        cat_level_2_id = request.args.get("catlevel2Id")
        no_pages = self.service.pages_count(cat_level_2_id)
        return no_pages
