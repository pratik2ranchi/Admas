from Api_Project.src.utilities.dbUtilities import DBUtilities
import random


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtilities()

    def get_random_products_from_DB(self, qty=1):
        sql = 'SELECT * FROM local.wp_posts WHERE post_type= "product" LIMIT 5000;'

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_by_ID(self,product_id):
        sql=f"SELECT * FROM local.wp_posts WHERE ID= {product_id};"

        return self.db_helper.execute_select(sql)

    def get_products_after_given_date(self, _date):
        sql=f'SELECT * FROM local.wp_posts WHERE post_type="product" AND post_date> "{_date}" LIMIT 10000;'

        return self.db_helper.execute_select(sql)

