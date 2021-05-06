from Api_Project.src.utilities.genericUtilities import generate_random_string
from Api_Project.src.helpers.products_helper import ProductHelper
from Api_Project.src.dao.products_dao import ProductsDAO
import pytest

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid26
def test_create_products():
    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = '10.99'

    # make the call
    product_rs = ProductHelper().call_create_product(payload)

    # verify the response is not empty

    assert product_rs, f"Create product api response is empty. payload :{payload}"
    assert product_rs['name'] == payload['name'], f"create product api call response has unexpected name. " \
                                                  f"Expected:{payload['name']}, Actual:{product_rs['name']} "

    # verify the product exist in db
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_ID(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create product, title in DB does not match title in api. " \
                                                           f"DB:{db_product['post_title']}, API:{payload['name']} "
