from Api_Project.src.utilities.dbUtilities import DBUtilities
import random


class CustomersDAO(object):
    def __init__(self):
        self.db_helper = DBUtilities()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql


