# coding: utf-8

"""
    NabooApi V1

    Here you have the first version of the naboo api to create checkout automatically

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from naboo.models.cash_out_orange_request import CashOutOrangeRequest

class TestCashOutOrangeRequest(unittest.TestCase):
    """CashOutOrangeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CashOutOrangeRequest:
        """Test CashOutOrangeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CashOutOrangeRequest`
        """
        model = CashOutOrangeRequest()
        if include_optional:
            return CashOutOrangeRequest(
                full_name = '',
                amount = 56,
                phone_number = ''
            )
        else:
            return CashOutOrangeRequest(
                full_name = '',
                amount = 56,
                phone_number = '',
        )
        """

    def testCashOutOrangeRequest(self):
        """Test CashOutOrangeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()