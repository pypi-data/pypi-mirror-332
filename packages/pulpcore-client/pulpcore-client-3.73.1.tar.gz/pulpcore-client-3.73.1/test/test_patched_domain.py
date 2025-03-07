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

from pulpcore.client.pulpcore.models.patched_domain import PatchedDomain

class TestPatchedDomain(unittest.TestCase):
    """PatchedDomain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedDomain:
        """Test PatchedDomain
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedDomain`
        """
        model = PatchedDomain()
        if include_optional:
            return PatchedDomain(
                name = 'z0',
                description = '0',
                pulp_labels = {
                    'key' : ''
                    },
                storage_class = 'pulpcore.app.models.storage.FileSystem',
                storage_settings = None,
                redirect_to_object_storage = True,
                hide_guarded_distributions = True
            )
        else:
            return PatchedDomain(
        )
        """

    def testPatchedDomain(self):
        """Test PatchedDomain"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
