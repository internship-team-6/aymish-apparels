from db_auth import DB_Auth
from db_statements import DB_Statements
from db_create import DB_Create


class DB_Ops:
    def __init__(self):
        DB_Create()
        self.db_auth = DB_Auth()
        self.db_statements = DB_Statements()
        id_select_statement = "SELECT {} FROM {}".format("id", "product")
        self.id_set = set(
            map(
                lambda x: x["id"],
                self.db_auth.conn.execute(id_select_statement).fetchall(),
            )
        )
        max_category_id_select_statement = "SELECT MAX({}) FROM {}".format(
            "id", "category"
        )
        self.cur_category_id = self.db_auth.conn.execute(
            max_category_id_select_statement
        ).fetchone()["max"]
        if self.cur_category_id is None:
            self.cur_category_id = "1"
        self.cat_level_1_name_id_map = {}

    def select_cat_level_1_name_id_list_with_subcategories(self):
        cat_level_1_name_id_list = self.db_auth.conn.execute(
            self.db_statements.cat_level_1_name_id_list_with_subcategories_select,
            ("1", "2", ""),
        ).fetchall()
        return cat_level_1_name_id_list

    def select_cat_level_2_name_list_parent_id(self, parent_id):
        cat_level_2_name_list = self.db_auth.conn.execute(
            self.db_statements.cat_level_2_name_list_with_parent_id_select,
            (parent_id, ""),
        ).fetchall()
        return cat_level_2_name_list

    def select_product_list_with_cat_level_1_id_cat_level_2_name(
        self, cat_level_1_id, cat_level_2_name
    ):
        product_list = self.db_auth.conn.execute(
            self.db_statements.product_list_with_cat_level_1_id_cat_level_2_name_select,
            (cat_level_1_id, cat_level_2_name),
        ).fetchall()
        return product_list

    def select_product_list_with_cat_level_1_id_cat_level_2_name_price_asc(
        self, cat_level_1_id, cat_level_2_name
    ):
        product_list = self.db_auth.conn.execute(
            self.db_statements.product_list_with_cat_level_1_id_cat_level_2_name_price_asc_select,
            (cat_level_1_id, cat_level_2_name),
        ).fetchall()
        return product_list

    def select_product_list_with_cat_level_1_id_cat_level_2_name_price_desc(
        self, cat_level_1_id, cat_level_2_name
    ):
        product_list = self.db_auth.conn.execute(
            self.db_statements.product_list_with_cat_level_1_id_cat_level_2_name_price_desc_select,
            (cat_level_1_id, cat_level_2_name),
        ).fetchall()
        return product_list

    def select_product_list_with_cat_level_1_id_cat_level_2_name_count(
        self, cat_level_1_id, cat_level_2_name
    ):
        count = self.db_auth.conn.execute(
            self.db_statements.product_list_with_cat_level_1_id_cat_level_2_name_count_select,
            (cat_level_1_id, cat_level_2_name),
        ).fetchone()
        return count

    def select_product_details_from_id(self, product_id):
        product_details = self.db_auth.conn.execute(
            self.db_statements.product_details_from_id_select, (product_id,)
        ).fetchone()
        return product_details

    def id_exists(self, unique_id):
        return unique_id in self.id_set

    def insert_product(self, data):
        unique_id = data["uniqueId"].strip()
        if self.id_exists(unique_id):
            return False
        product_insert_data = (
            unique_id,
            data["name"].strip(),
            data["title"].strip(),
            data["productImage"].strip(),
            data["price"],
            data.get("productDescription", "").strip(),
            data["availability"].strip(),
        )
        self.db_auth.conn.execute(
            self.db_statements.product_table_insert, product_insert_data
        )
        self.db_auth.conn.commit()
        self.id_set.add(unique_id)
        return True

    def increment_category_id(self):
        self.cur_category_id = str(int(self.cur_category_id) + 1)

    def insert_category_cat_level_1(self, data):
        name = data["catlevel1Name"].strip()
        category_cat_level_1_insert_data = (self.cur_category_id, name, "1")
        self.db_auth.conn.execute(
            self.db_statements.category_table_cat_level_1_insert,
            category_cat_level_1_insert_data,
        )
        self.db_auth.conn.commit()
        self.cat_level_1_name_id_map[name] = self.cur_category_id
        self.increment_category_id()
        return True

    def insert_category_cat_level_2(self, data):
        cat_level_1_name = data["catlevel1Name"].strip()
        name = data.get("catlevel2Name", "").strip()
        parent_id = self.cat_level_1_name_id_map[cat_level_1_name]
        product_id = data["uniqueId"].strip()
        category_cat_level_2_insert_data = (
            self.cur_category_id,
            name,
            "2",
            parent_id,
            product_id,
        )
        self.db_auth.conn.execute(
            self.db_statements.category_table_cat_level_2_insert,
            category_cat_level_2_insert_data,
        )
        self.db_auth.conn.commit()
        self.increment_category_id()
        return True

    def insert(self, data):
        if not self.insert_product(data):
            return False
        name = data["catlevel1Name"].strip()
        if not self.cat_level_1_name_id_map.get(name, ""):
            self.insert_category_cat_level_1(data)
        self.insert_category_cat_level_2(data)
        return True
