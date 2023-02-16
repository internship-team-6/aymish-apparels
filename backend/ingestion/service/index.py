from ingestion.dao.index import DAO


class Service:
    def __init__(self):
        self.dao = DAO()

    def insert_data(self, product_list):
        for product in product_list:
            cat_level_2_name = product.get("catlevel2Name", "").strip()
            if not cat_level_2_name:
                continue
            unique_id = product["uniqueId"].strip()
            name = product["name"].strip()
            title = product["title"].strip()
            price = product["price"]
            description = product.get("productDescription", "").strip()
            image = product["productImage"].strip()
            availability = product["availability"].strip()
            cat_level_1_name = product["catlevel1Name"].strip()
            self.dao.insert(
                unique_id,
                name,
                title,
                image,
                price,
                description,
                availability,
                cat_level_1_name,
                cat_level_2_name,
            )
