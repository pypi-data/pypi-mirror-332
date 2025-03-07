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

from pulpcore.client.pulpcore.models.paginated_rbac_content_guard_response_list import PaginatedRBACContentGuardResponseList

class TestPaginatedRBACContentGuardResponseList(unittest.TestCase):
    """PaginatedRBACContentGuardResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedRBACContentGuardResponseList:
        """Test PaginatedRBACContentGuardResponseList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedRBACContentGuardResponseList`
        """
        model = PaginatedRBACContentGuardResponseList()
        if include_optional:
            return PaginatedRBACContentGuardResponseList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    pulpcore.client.pulpcore.models.rbac_content_guard_response.RBACContentGuardResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        description = '', 
                        users = [
                            pulpcore.client.pulpcore.models.group_user_response.GroupUserResponse(
                                username = '', 
                                pulp_href = '', 
                                prn = '', )
                            ], 
                        groups = [
                            pulpcore.client.pulpcore.models.group_response.GroupResponse(
                                name = '', 
                                pulp_href = '', 
                                prn = '', 
                                id = 56, )
                            ], )
                    ]
            )
        else:
            return PaginatedRBACContentGuardResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulpcore.models.rbac_content_guard_response.RBACContentGuardResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        description = '', 
                        users = [
                            pulpcore.client.pulpcore.models.group_user_response.GroupUserResponse(
                                username = '', 
                                pulp_href = '', 
                                prn = '', )
                            ], 
                        groups = [
                            pulpcore.client.pulpcore.models.group_response.GroupResponse(
                                name = '', 
                                pulp_href = '', 
                                prn = '', 
                                id = 56, )
                            ], )
                    ],
        )
        """

    def testPaginatedRBACContentGuardResponseList(self):
        """Test PaginatedRBACContentGuardResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
