from flask import request
from flask_restful import Resource
from recommendations.service.index import RecommendationsService

class RecommendationsControl(Resource):
    def __init__(self):
        self.service=RecommendationsService()

    def get(self):

        # obtain parameters
        product_id=request.args.get("uniqueId")
        
        # get list of recommended products
        product_list=self.service.select_recommended_product_list(product_id)
        return product_list
