import pytest
import logging as logger
from Api_Project.src.utilities.requestUtilities import RequestUtilities


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtilities()
    rs_api = req_helper.get('customers')
