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

from pulpcore.client.pulpcore.models.artifact_response import ArtifactResponse

class TestArtifactResponse(unittest.TestCase):
    """ArtifactResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArtifactResponse:
        """Test ArtifactResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArtifactResponse`
        """
        model = ArtifactResponse()
        if include_optional:
            return ArtifactResponse(
                pulp_href = '',
                prn = '',
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                file = '',
                size = 56,
                md5 = '',
                sha1 = '',
                sha224 = '',
                sha256 = '',
                sha384 = '',
                sha512 = ''
            )
        else:
            return ArtifactResponse(
                file = '',
        )
        """

    def testArtifactResponse(self):
        """Test ArtifactResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
