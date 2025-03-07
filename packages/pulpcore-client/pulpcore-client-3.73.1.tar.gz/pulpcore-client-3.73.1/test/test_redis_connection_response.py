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

from pulpcore.client.pulpcore.models.redis_connection_response import RedisConnectionResponse

class TestRedisConnectionResponse(unittest.TestCase):
    """RedisConnectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RedisConnectionResponse:
        """Test RedisConnectionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RedisConnectionResponse`
        """
        model = RedisConnectionResponse()
        if include_optional:
            return RedisConnectionResponse(
                connected = True
            )
        else:
            return RedisConnectionResponse(
                connected = True,
        )
        """

    def testRedisConnectionResponse(self):
        """Test RedisConnectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
