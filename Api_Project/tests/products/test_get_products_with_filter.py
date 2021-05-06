import pytest
from Api_Project.src.dao.products_dao import ProductsDAO
from Api_Project.src.helpers.products_helper import ProductHelper
from datetime import datetime, timedelta
import pdb


@pytest.mark.regression
class TestProductWithFilters(object):

    @pytest.mark.tcid51
    def test_list_product_with_filter_after(self):
        # create data
        x_days_from_today = 300

        _after_created_data = datetime.now().replace(microsecond=0) - timedelta(x_days_from_today)
        after_created_date = _after_created_data.isoformat()

        # temp_date = datetime.now() - timedelta(days=x_days_from_today)
        # after_created_date = temp_date.strftime('%Y-%m-%d %H:%M:%S')
        # make the call
        payload = dict()
        payload['after'] = after_created_date
        rs_api = ProductHelper().call_list_products(payload)
        assert rs_api, f"Empty response for 'list products with filter"

        # get data from db
        db_product = ProductsDAO().get_products_after_given_date(after_created_date)

        # verify the response matches DB

        assert len(rs_api) == len(db_product), f"List product with filter, 'after' returned unexpected no of products. " \
                                               f"Expected: {len(db_product)}, Actual:{len(rs_api)}"

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_product]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff


