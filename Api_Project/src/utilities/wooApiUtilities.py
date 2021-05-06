from woocommerce import API
from Api_Project.src.configs.hosts_configs import Woo_API_HOSTS
import os
import logging as logger


class WooApiUtilities(object):
    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = Woo_API_HOSTS[self.env]
        self.wcapi = API(
            url=self.base_url,
            consumer_key='ck_0085a54be0a5de70ef8378e0f25cbc5e25965e0d',
            consumer_secret='cs_17f2fb28b85a3e9cb7254cc31ac25ebbac90d703',
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code. expected:{self.status_code}"

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        rs_api = self.wcapi.get(wc_endpoint, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f'api get response: {self.rs_json}')
        return self.rs_json
