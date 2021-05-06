from Api_Project.src.configs.hosts_configs import API_HOSTS

from requests_oauthlib import OAuth1
import requests
import os
import json
import logging as logger


class RequestUtilities(object):
    def __init__(self):

        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1('ck_0085a54be0a5de70ef8378e0f25cbc5e25965e0d','cs_17f2fb28b85a3e9cb7254cc31ac25ebbac90d703')

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code. expected:{self.status_code}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {'Content-Type': 'application/json'}

        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code=expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f'api post response: {self.rs_json}')

        return self.rs_json

    def get (self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {'Content-Type': 'application/json'}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f'api get response: {self.rs_json}')

        return self.rs_json

