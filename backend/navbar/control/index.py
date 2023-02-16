from flask_restful import Resource
from navbar.service.index import Service


class NavBarControl(Resource):
    def __init__(self):
        self.service = Service()

    def get(self):
        categories = self.service.select_categories()
        return categories
