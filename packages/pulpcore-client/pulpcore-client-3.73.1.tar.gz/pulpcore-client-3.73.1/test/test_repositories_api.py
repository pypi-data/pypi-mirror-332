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

from pulpcore.client.pulpcore.api.repositories_api import RepositoriesApi


class TestRepositoriesApi(unittest.TestCase):
    """RepositoriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RepositoriesApi()

    def tearDown(self) -> None:
        pass

    def test_list(self) -> None:
        """Test case for list

        List repositories
        """
        pass


if __name__ == '__main__':
    unittest.main()
