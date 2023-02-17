from recommendations.service.index import Service
from flask import request
from flask_restful import Resource

class RecommendationsControl(Resource):
    def __init__(self):
        self.service=Service()

    def get(self):
        product_name=request.args.get("productName")
        product_list=self.service.select_recommended_product_list(product_name)
        return product_list
