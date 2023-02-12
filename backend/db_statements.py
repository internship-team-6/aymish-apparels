class DB_Statements:
    def __init__(self):
        self.PRODUCT_TABLE_IF_NOT_EXISTS_CREATE = """
        CREATE TABLE IF NOT EXISTS product
        (
          id TEXT NOT NULL,
          name TEXT NOT NULL,
          title TEXT NOT NULL,
          image TEXT NOT NULL,
          price FLOAT NOT NULL,
          description TEXT,
          availability BOOLEAN NOT NULL,
          PRIMARY KEY (id)
        );
        """
        self.CATEGORY_TABLE_IF_NOT_EXISTS_CREATE = """
        CREATE TABLE IF NOT EXISTS category
        (
          id TEXT NOT NULL,
          name TEXT,
          level TEXT,
          parentId TEXT,
          productId TEXT,
          PRIMARY KEY (id),
          FOREIGN KEY (parentId) REFERENCES category(id) ON UPDATE CASCADE ON DELETE CASCADE,
          FOREIGN KEY (productId) REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
        self.product_table_insert = "INSERT INTO {} ({}, {}, {}, {}, {}, {}, {}) VALUES (%s, %s, %s, %s, %s, %s, %s)".format(
            "product",
            "id",
            "name",
            "title",
            "image",
            "price",
            "description",
            "availability",
        )
        self.category_table_cat_level_1_insert = (
            "INSERT INTO {} ({}, {}, {}) VALUES (%s, %s, %s)".format(
                "category", "id", "name", "level"
            )
        )
        self.category_table_cat_level_2_insert = (
            "INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (%s, %s, %s, %s, %s)".format(
                "category", "id", "name", "level", "parentId", "productId"
            )
        )
        self.cat_level_1_name_id_list_with_subcategories_select = "SELECT {}, {} FROM {} WHERE {}=%s AND {} in (SELECT DISTINCT {} from {} WHERE {}=%s AND TRIM({})>%s) ORDER BY {} ASC".format(
            "name",
            "id",
            "category",
            "level",
            "id",
            "parentId",
            "category",
            "level",
            "name",
            "id",
        )
        self.product_list_with_cat_level_1_id_cat_level_2_name_select = "SELECT {}, {}, {}, {} FROM {} WHERE {} IN (SELECT {} FROM {} WHERE {}=%s AND {}=%s)".format(
            "id",
            "title",
            "image",
            "price",
            "product",
            "id",
            "productId",
            "category",
            "parentId",
            "name",
        )
        self.product_list_with_cat_level_1_id_cat_level_2_name_price_asc_select = (
            "{} ORDER BY {} ASC".format(
                self.product_list_with_cat_level_1_id_cat_level_2_name_select, "price"
            )
        )
        self.product_list_with_cat_level_1_id_cat_level_2_name_price_desc_select = (
            "{} ORDER BY {} DESC".format(
                self.product_list_with_cat_level_1_id_cat_level_2_name_select, "price"
            )
        )
        self.product_details_from_id_select = "SELECT {} FROM {} WHERE {}=%s".format(
            "*", "product", "id"
        )
        self.cat_level_2_name_list_with_parent_id_select = "SELECT DISTINCT name FROM category WHERE parentId=%s AND TRIM(name)>%s".format(
            "name", "category", "parentId", "name"
        )
