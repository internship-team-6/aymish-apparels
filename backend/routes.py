from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_cors import CORS
import yaml
from yaml.loader import SafeLoader
import requests

from db_ops import DB_Ops
from cache_ops import Cache_Ops


app = Flask(__name__)
api = Api(app)
CORS(app)


class Ingestion(Resource):
    def __init__(self):
        self.db_ops = DB_Ops()

    def post(self):
        data_iter = request.json
        for data in data_iter:
            res = self.db_ops.insert(data)
            if not res:
                print("{} already exists".format(data["uniqueId"]))
        self.db_ops.db_auth.conn.commit()
        return "Data ingestion done"


api.add_resource(Ingestion, "/ingestion")


class SearchProductList(Resource):
    def __init__(self):
        config_file = "./.config/search/config.yaml"
        with open(config_file) as cf:
            config_dict = yaml.load(cf, Loader=SafeLoader)
        self.api = config_dict["unbxd_search_api"]
        self.rows_count = int(config_dict["rows_count"])
        self.db_ops = DB_Ops()

    def get(self):
        sort_order = request.args.get("sort", "")
        q = request.args.get("q", "shirts")
        params = {"q": q, "rows": self.rows_count}
        if sort_order.lower() == "asc":
            params["sort"] = "price asc"
        elif sort_order.lower() == "desc":
            params["sort"] = "price desc"
        resp = requests.get(self.api, params).json()
        prod_list = resp["response"]["products"]
        count = len(prod_list)

        product_list = []

        for products_counter in range(0, count):
            data = prod_list[products_counter]
            prod_id = data["uniqueId"].strip()
            prod_name = data["name"].strip()
            prod_title = data["title"].strip()
            prod_price = data["price"]
            prod_description = data.get("productDescription", "").strip()
            prod_image = data["productImage"].strip()
            prod_availability = data["availability"].strip()
            prod_cat_level_1_name = data["catlevel1Name"].strip()
            prod_cat_level_2_name = data.get("catlevel2Name", "").strip()

            product_list.append(
                {
                    "id": prod_id,
                    "name": prod_name,
                    "title": prod_title,
                    "description": prod_description,
                    "image": prod_image,
                    "price": prod_price,
                }
            )

            self.db_ops.insert_product(data)
        return product_list


api.add_resource(SearchProductList, "/search")


class NavBar(Resource):
    def __init__(self):
        self.db_ops = DB_Ops()
        self.cache_ops = Cache_Ops()

    def get(self):
        r_key = "navbar->{}".format("categories")
        categories = self.cache_ops.get(r_key)
        if categories is None:
            categories = (
                self.db_ops.select_cat_level_1_name_id_list_with_subcategories()
            )
            self.cache_ops.set(r_key, categories)
        return categories


api.add_resource(NavBar, "/navbar")


class DropDown(Resource):
    def __init__(self):
        self.db_ops = DB_Ops()
        self.cache_ops = Cache_Ops()

    def get(self):
        cat_level_1_id = request.args.get("catlevel1Id")
        r_key = "dropdown->{}".format(cat_level_1_id)
        sub_categories = self.cache_ops.get(r_key)
        if sub_categories is None:
            sub_categories = self.db_ops.select_cat_level_2_name_list_parent_id(
                cat_level_1_id
            )
            self.cache_ops.set(r_key, sub_categories)
        return sub_categories


api.add_resource(DropDown, "/dropdown")


class CategoryProductList(Resource):
    def __init__(self):
        self.db_ops = DB_Ops()
        self.cache_ops = Cache_Ops()

    def get(self):
        cat_level_1_id = request.args.get("catlevel1Id")
        cat_level_2_name = request.args.get("catlevel2Name")
        sort_order = request.args.get("sort", "")
        if sort_order in ("asc", "desc"):
            r_key = "category-product-list->{}->{}->{}".format(
                cat_level_1_id, cat_level_2_name, sort_order
            )
        else:
            r_key = "category-product-list->{}->{}".format(
                cat_level_1_id, cat_level_2_name
            )
        product_list = self.cache_ops.get(r_key)
        if product_list is None:
            if sort_order == "asc":
                product_list = self.db_ops.select_product_list_with_cat_level_1_id_cat_level_2_name_price_asc(
                    cat_level_1_id, cat_level_2_name
                )
            elif sort_order == "desc":
                product_list = self.db_ops.select_product_list_with_cat_level_1_id_cat_level_2_name_price_desc(
                    cat_level_1_id, cat_level_2_name
                )
            else:
                product_list = self.db_ops.select_product_list_with_cat_level_1_id_cat_level_2_name(
                    cat_level_1_id, cat_level_2_name
                )
            self.cache_ops.set(r_key, product_list)
        return product_list


api.add_resource(CategoryProductList, "/category-product-list")


class Product(Resource):
    def __init__(self):
        self.db_ops = DB_Ops()
        self.cache_ops = Cache_Ops()

    def get(self):
        product_id = request.args.get("uniqueId")
        r_key = "product->{}".format(product_id)
        product_details = self.cache_ops.get(r_key)
        if product_details is None:
            product_details = self.db_ops.select_product_details_from_id(product_id)
            self.cache_ops.set(r_key, product_details)
        return product_details


api.add_resource(Product, "/product")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
