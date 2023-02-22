from ingestion.dao.index import IngestionDAO


class IngestionService:
    def __init__(self):
        self.dao = IngestionDAO()

    def insert_data(self, product_list):
        for product in product_list:
            cat_level_2_name = product.get("catlevel2Name", "").strip()
            
            # don't add records having empty values for cat level 2 or no field for cat level 2
            if not cat_level_2_name:
                continue

            # extract values to be added to the database
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
