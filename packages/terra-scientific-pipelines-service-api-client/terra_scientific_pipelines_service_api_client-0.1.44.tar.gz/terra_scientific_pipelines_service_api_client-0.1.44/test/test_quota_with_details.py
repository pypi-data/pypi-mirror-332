# coding: utf-8

"""
    Terra Scientific Pipelines Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from teaspoons_client.models.quota_with_details import QuotaWithDetails

class TestQuotaWithDetails(unittest.TestCase):
    """QuotaWithDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuotaWithDetails:
        """Test QuotaWithDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuotaWithDetails`
        """
        model = QuotaWithDetails()
        if include_optional:
            return QuotaWithDetails(
                pipeline_name = '',
                quota_limit = 56,
                quota_consumed = 56,
                quota_units = ''
            )
        else:
            return QuotaWithDetails(
                pipeline_name = '',
                quota_limit = 56,
                quota_consumed = 56,
                quota_units = '',
        )
        """

    def testQuotaWithDetails(self):
        """Test QuotaWithDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
