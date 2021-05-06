from Api_Project.src.utilities.genericUtilities import generate_random_email_password
from Api_Project.src.utilities.requestUtilities import RequestUtilities


class CustomersHelper(object):
    def __init__(self):
        self.requests_utilities = RequestUtilities()

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = generate_random_email_password()
            email = ep["email"]

        if not password:
            password = "Password1"

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_user_json=self.requests_utilities.post('customers', payload=payload, expected_status_code=201)

        return create_user_json


