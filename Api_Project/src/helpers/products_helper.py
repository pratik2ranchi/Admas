from Api_Project.src.utilities.requestUtilities import RequestUtilities


class ProductHelper(object):
    def __init__(self):
        self.requests_utilities = RequestUtilities()

    def get_product_by_id(self, product_id):
        return self.requests_utilities.get(f"products/{product_id}")

    def call_create_product(self, payload):
        rs_api = self.requests_utilities.post('products', payload=payload, expected_status_code=201)

        return rs_api

    def call_list_products(self, payload=None):
        return self.requests_utilities.get('products', payload=payload)
