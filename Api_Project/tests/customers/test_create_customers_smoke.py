import pytest
import logging as logger
from Api_Project.src.utilities.genericUtilities import generate_random_email_password
from Api_Project.src.helpers.customers_helper import CustomersHelper
from Api_Project.src.dao.customers_dao import CustomersDAO
from Api_Project.src.helpers.customers_helper import RequestUtilities


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("Create new Customer")

    rand_info = generate_random_email_password()
    email = rand_info['email']
    password = rand_info['password']

    # make the api call
    cust_obj = CustomersHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f'Create Customer api return wrong email. Email:{email}'
    assert cust_api_info['first_name'] == ''

    # verify customer is created in db
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customers_fails_for_existing_email():
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    # call the api
    req_helper = RequestUtilities()
    payload = {'email': existing_email, 'password': 'Password1'}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    import pdb;
    pdb.set_trace()
