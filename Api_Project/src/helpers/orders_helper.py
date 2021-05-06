import os
import json


class OrdersHelper(object):
    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))

    def createOrder(self, additional_args=None):
        payload_tmeplate = os.path.join(self.cur_file_dir, '..', 'data/create_order_payload.json')
        with open(payload_tmeplate) as f:
            payload = json.load(f)

        if additional_args:
            assert isinstance(additional_args, dict), f"parameter 'additional args' must be dictionary"
            payload.update(additional_args)

        import pdb;
        pdb.set_trace()
