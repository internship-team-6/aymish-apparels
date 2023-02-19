from flask_restful import Resource
from flask import request
from category_product_list.service.index import CategoryProductListService


class CategoryProductListControl(Resource):
    def __init__(self):
        self.service = CategoryProductListService()

    def get(self):
        cat_level_2_id = request.args.get("catlevel2Id")
        sort_order = request.args.get("sort", "")
        page = int(request.args.get("page"))
        category_product_list = self.service.select_product_list(
            cat_level_2_id, sort_order, page
        )
        return category_product_list
