from flask_restful import Resource
from flask import request
from search_product_list.service.index import SearchProductListService


class SearchProductListControl(Resource):
    def __init__(self):
        self.service = SearchProductListService()

    def get(self):
        sort_order = request.args.get("sort", "")
        q = request.args.get("q", "*")
        page = request.args.get("page")
        search_product_list = self.service.select_product_list(q, sort_order, page)
        return search_product_list
