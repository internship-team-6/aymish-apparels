from flask import request
from flask_restful import Resource
from ingestion.service.index import IngestionService


class IngestionControl(Resource):
    def __init__(self):
        self.service = Service()

    def post(self):
        product_list = request.json
        self.service.insert_data(product_list)
        return True
