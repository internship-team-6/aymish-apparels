from flask import request
from flask_restful import Resource
from product.service.index import ProductService


class ProductControl(Resource):
    def __init__(self):
        self.service = ProductService()

    def get(self):
        product_id = request.args.get("uniqueId")
        product_details = self.service.select_product(product_id)
        return product_details
