import os


class CredentialsUtilities(object):
    def __init__(self):
        self

    @staticmethod
    def get_wc_api_keys():
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or wc_secret:
            raise Exception('the api credentials must be in env variable ')
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}
