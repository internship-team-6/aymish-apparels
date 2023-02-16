from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from common.dao.db_create import DB_Create

db_create = DB_Create()
db_create.create_category_table_if_not_exists()
db_create.create_product_table_if_not_exists()

from ingestion.control.index import IngestionControl
from search_product_list.control.index import SearchProductListControl
from navbar.control.index import NavBarControl
from dropdown.control.index import DropDownControl
from category_product_list.control.index import CategoryProductListControl
from product.control.index import ProductControl
from name_tree.control.index import NameTreeControl
from category_pagination.control.index import CategoryPaginationControl

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(IngestionControl, "/ingestion")
api.add_resource(SearchProductListControl, "/search")
api.add_resource(NavBarControl, "/navbar")
api.add_resource(DropDownControl, "/dropdown")
api.add_resource(CategoryProductListControl, "/category-product-list")
api.add_resource(ProductControl, "/product")
api.add_resource(NameTreeControl, "/name-tree")
api.add_resource(CategoryPaginationControl, "/category-pagination")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0")
