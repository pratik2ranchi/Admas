import pytest
from Api_Project.src.dao.products_dao import ProductsDAO
from Api_Project.src.utilities.requestUtilities import RequestUtilities
from Api_Project.src.helpers.products_helper import ProductHelper

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestUtilities()
    rs_api = req_helper.get(endpoint='products')

    assert rs_api, f"Get all product end point returned nothing."


@pytest.mark.tcid25
def test_get_product_by_id():
    # get a product from DB
    rand_product = ProductsDAO.get_random_products_from_DB(1)
    rand_product_id = rand_product[0]['ID']

    # make a api cll
    product_helper = ProductHelper()
    rs_api = ProductHelper.get_product_by_id(rand_product_id)

    import pdb;
    pdb.set_trace()
