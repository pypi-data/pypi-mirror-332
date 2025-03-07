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

from pulpcore.client.pulpcore.api.content_openpgp_signature_api import ContentOpenpgpSignatureApi


class TestContentOpenpgpSignatureApi(unittest.TestCase):
    """ContentOpenpgpSignatureApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContentOpenpgpSignatureApi()

    def tearDown(self) -> None:
        pass

    def test_list(self) -> None:
        """Test case for list

        List open pgp signatures
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Inspect an open pgp signature
        """
        pass


if __name__ == '__main__':
    unittest.main()
