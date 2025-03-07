# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pulpcore.client.pulpcore.models.composite_content_guard import CompositeContentGuard

class TestCompositeContentGuard(unittest.TestCase):
    """CompositeContentGuard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompositeContentGuard:
        """Test CompositeContentGuard
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompositeContentGuard`
        """
        model = CompositeContentGuard()
        if include_optional:
            return CompositeContentGuard(
                name = '0',
                description = '0',
                guards = [
                    ''
                    ]
            )
        else:
            return CompositeContentGuard(
                name = '0',
        )
        """

    def testCompositeContentGuard(self):
        """Test CompositeContentGuard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
