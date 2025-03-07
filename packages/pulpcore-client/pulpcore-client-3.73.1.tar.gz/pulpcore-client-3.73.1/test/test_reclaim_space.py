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

from pulpcore.client.pulpcore.models.reclaim_space import ReclaimSpace

class TestReclaimSpace(unittest.TestCase):
    """ReclaimSpace unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReclaimSpace:
        """Test ReclaimSpace
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReclaimSpace`
        """
        model = ReclaimSpace()
        if include_optional:
            return ReclaimSpace(
                repo_hrefs = [
                    null
                    ],
                repo_versions_keeplist = [
                    ''
                    ]
            )
        else:
            return ReclaimSpace(
                repo_hrefs = [
                    null
                    ],
        )
        """

    def testReclaimSpace(self):
        """Test ReclaimSpace"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
