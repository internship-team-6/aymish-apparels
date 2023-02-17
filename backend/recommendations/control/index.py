from recommendations.service.index import Service
from flask import request
from flask_restful import Resource

class RecommendationsControl(Resource):
    def __init__(self):
        self.service=Service()

    def get(self):
        product_id=request.args.get("uniqueId")
        product_list=self.service.select_recommended_product_list(product_id)
        return product_list
