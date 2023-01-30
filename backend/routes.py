from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import yaml
from yaml.loader import SafeLoader
import requests

# import json
from db_ops import DB_Ops


app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def __init__(self):
        self.db_ops = DB_Ops()
        self.conn = self.db_ops.conn

    def get(self):
        products = self.db_ops.select_products()
        categories = self.db_ops.select_categories()
        return {"products": products, "categories": categories}


api.add_resource(Home, "/home")


class Ingestion(Resource):
    def __init__(self):
        self.db_ops = DB_Ops()
        self.conn = self.db_ops.conn

    def post(self):
        data_iter = request.json
        for data in data_iter:
            res = self.db_ops.insert(data)
            if not res:
                print("{} already exists".format(data["uniqueId"]))
        self.conn.commit()
        return "Data ingestion done"

    def put(self):
        data_iter = request.json
        for data in data_iter:
            self.db_ops.update(data)
        self.conn.commit()
        return "Data updation done"


api.add_resource(Ingestion, "/ingestion")


class Search(Resource):
    def __init__(self):
        config_file = "./.config/search/config.yaml"
        with open(config_file) as cf:
            api_dict = yaml.load(cf, Loader=SafeLoader)
        self.api = api_dict["unbxd_search_api"]
        self.db_ops=DB_Ops()

    def get(self):
        rows_count = 6
        order = request.args.get("order")
        params = {"q": request.args.get("q"), "rows": rows_count}
        if order.lower() == "asc":
            params["sort"] = "price asc"
        elif order.lower() == "desc":
            params["sort"] = "price desc"
        resp = requests.get(self.api, params).json()
        count = len(resp["response"]["products"])

        prod_list=resp["response"]["products"]

        products = []
        categories = []

        for products_counter in range(0, count):
            prod_id=prod_list[products_counter]['uniqueId'].strip()
            prod_name=prod_list[products_counter]['name'].strip()
            prod_title=prod_list[products_counter]['title'].strip()
            prod_price=prod_list[products_counter]['price']
            prod_desc=prod_list[products_counter].get('productDescription','').strip()
            prod_img=prod_list[products_counter]['productImage'].strip()
            prod_avail=prod_list[products_counter]['availability'].strip()
            prod_cat_lvl1=prod_list[products_counter]['catlevel1Name'].strip()
            prod_cat_lvl2=prod_list[products_counter].get('catlevel2Name','').strip()

            products.append((prod_id, prod_name, prod_title, prod_desc, prod_img))
            categories.append((prod_id, prod_cat_lvl1, prod_cat_lvl2))

            data={'uniqueId': prod_id, 'name': prod_name, 'title': prod_title, 'price': prod_price, 'productDescription': prod_desc, 'productImage': prod_img, 'availability': prod_avail, 'catlevel1Name': prod_cat_lvl1, 'catlevel2Name': prod_cat_lvl2}
            insert_status=self.db_ops.insert(data)

        return {'products': products, 'categories': categories}


api.add_resource(Search, "/search")

if __name__ == "__main__":
    app.run(debug=True)
