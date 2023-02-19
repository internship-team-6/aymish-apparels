import yaml
from yaml.loader import SafeLoader
import requests
from search_product_list.dao.index import SearchProductListDAO


class SearchProductListService:
    def __init__(self):
        config_file = "./.config/search/config.yaml"
        with open(config_file) as cf:
            config_dict = yaml.load(cf, Loader=SafeLoader)
        self.api = config_dict["unbxd_search_api"]
        self.rows_limit = config_dict["rows_limit"]
        self.dao = SearchProductListDAO()

    def select_product_list(self, q, sort_order, page):
        params = {"q": q, "rows": self.rows_limit, "page": page}
        if sort_order.lower() == "asc":
            params["sort"] = "price asc"
        elif sort_order.lower() == "desc":
            params["sort"] = "price desc"
        resp = requests.get(self.api, params).json()
        prod_list = resp["response"]["products"]

        product_count = resp["response"]["numberOfProducts"]
        no_pages = product_count // self.rows_limit + (
            product_count % self.rows_limit and 1
        )
        product_list = []

        for counter in range(0, len(prod_list)):
            data = prod_list[counter]
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
            if prod_cat_level_2_name:
                self.dao.insert(
                    prod_id,
                    prod_name,
                    prod_title,
                    prod_image,
                    prod_price,
                    prod_description,
                    prod_availability,
                    prod_cat_level_1_name,
                    prod_cat_level_2_name,
                )
        return {"product_list": product_list, "pages": no_pages}
