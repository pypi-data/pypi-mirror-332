# coding: utf-8

"""
    Terra Scientific Pipelines Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from teaspoons_client.models.pipeline_user_provided_input_definition import PipelineUserProvidedInputDefinition

class TestPipelineUserProvidedInputDefinition(unittest.TestCase):
    """PipelineUserProvidedInputDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PipelineUserProvidedInputDefinition:
        """Test PipelineUserProvidedInputDefinition
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PipelineUserProvidedInputDefinition`
        """
        model = PipelineUserProvidedInputDefinition()
        if include_optional:
            return PipelineUserProvidedInputDefinition(
                name = '',
                type = '',
                is_required = True,
                file_suffix = ''
            )
        else:
            return PipelineUserProvidedInputDefinition(
        )
        """

    def testPipelineUserProvidedInputDefinition(self):
        """Test PipelineUserProvidedInputDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
