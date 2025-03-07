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

from pulpcore.client.pulpcore.models.object_roles_response import ObjectRolesResponse

class TestObjectRolesResponse(unittest.TestCase):
    """ObjectRolesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectRolesResponse:
        """Test ObjectRolesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectRolesResponse`
        """
        model = ObjectRolesResponse()
        if include_optional:
            return ObjectRolesResponse(
                roles = [
                    pulpcore.client.pulpcore.models.nested_role_response.NestedRoleResponse(
                        users = [
                            ''
                            ], 
                        groups = [
                            ''
                            ], 
                        role = '', )
                    ]
            )
        else:
            return ObjectRolesResponse(
                roles = [
                    pulpcore.client.pulpcore.models.nested_role_response.NestedRoleResponse(
                        users = [
                            ''
                            ], 
                        groups = [
                            ''
                            ], 
                        role = '', )
                    ],
        )
        """

    def testObjectRolesResponse(self):
        """Test ObjectRolesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
