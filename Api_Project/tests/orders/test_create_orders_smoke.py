import pytest
import pdb
from Api_Project.src.dao.products_dao import ProductsDAO
from Api_Project.src.helpers.orders_helper import OrdersHelper


@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()

    # get a product from DB
    product_dao = ProductsDAO()
    rand_product = product_dao.get_random_products_from_DB(1)
    product_id = rand_product[0]['ID']

    # make the call
    order_helper.createOrder()

    # verify the response

    # verify DB
