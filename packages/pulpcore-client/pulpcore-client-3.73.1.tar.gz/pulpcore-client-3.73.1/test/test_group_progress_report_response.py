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

from pulpcore.client.pulpcore.models.group_progress_report_response import GroupProgressReportResponse

class TestGroupProgressReportResponse(unittest.TestCase):
    """GroupProgressReportResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupProgressReportResponse:
        """Test GroupProgressReportResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupProgressReportResponse`
        """
        model = GroupProgressReportResponse()
        if include_optional:
            return GroupProgressReportResponse(
                message = '',
                code = '',
                total = 56,
                done = 56,
                suffix = ''
            )
        else:
            return GroupProgressReportResponse(
        )
        """

    def testGroupProgressReportResponse(self):
        """Test GroupProgressReportResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
