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

from pulpcore.client.pulpcore.models.paginated_repository_response_list import PaginatedRepositoryResponseList

class TestPaginatedRepositoryResponseList(unittest.TestCase):
    """PaginatedRepositoryResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedRepositoryResponseList:
        """Test PaginatedRepositoryResponseList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedRepositoryResponseList`
        """
        model = PaginatedRepositoryResponseList()
        if include_optional:
            return PaginatedRepositoryResponseList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    pulpcore.client.pulpcore.models.repository_response.RepositoryResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        versions_href = '', 
                        pulp_labels = {
                            'key' : ''
                            }, 
                        latest_version_href = '', 
                        name = '', 
                        description = '', 
                        retain_repo_versions = 1, 
                        remote = '', )
                    ]
            )
        else:
            return PaginatedRepositoryResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulpcore.models.repository_response.RepositoryResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        versions_href = '', 
                        pulp_labels = {
                            'key' : ''
                            }, 
                        latest_version_href = '', 
                        name = '', 
                        description = '', 
                        retain_repo_versions = 1, 
                        remote = '', )
                    ],
        )
        """

    def testPaginatedRepositoryResponseList(self):
        """Test PaginatedRepositoryResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
