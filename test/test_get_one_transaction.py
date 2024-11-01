# coding: utf-8

"""
    NabooApi V1

    Here you have the first version of the naboo api to create checkout automatically

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from naboo.models.get_one_transaction import GetOneTransaction

class TestGetOneTransaction(unittest.TestCase):
    """GetOneTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetOneTransaction:
        """Test GetOneTransaction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOneTransaction`
        """
        model = GetOneTransaction()
        if include_optional:
            return GetOneTransaction(
                order_id = '',
                method_of_payment = [
                    'WAVE'
                    ],
                amount = 56,
                amount_to_pay = 56,
                currency = '',
                created_at = '',
                transaction_status = 'pending',
                products = [
                    naboo.models.product_model.ProductModel(
                        name = '', 
                        category = '', 
                        amount = 56, 
                        quantity = 56, 
                        description = '', )
                    ],
                is_done = True,
                is_escrow = True,
                is_merchant = True,
                checkout_url = ''
            )
        else:
            return GetOneTransaction(
                order_id = '',
                method_of_payment = [
                    'WAVE'
                    ],
                amount = 56,
                amount_to_pay = 56,
                currency = '',
                created_at = '',
                transaction_status = 'pending',
                products = [
                    naboo.models.product_model.ProductModel(
                        name = '', 
                        category = '', 
                        amount = 56, 
                        quantity = 56, 
                        description = '', )
                    ],
                is_done = True,
                is_escrow = True,
                is_merchant = True,
                checkout_url = '',
        )
        """

    def testGetOneTransaction(self):
        """Test GetOneTransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
