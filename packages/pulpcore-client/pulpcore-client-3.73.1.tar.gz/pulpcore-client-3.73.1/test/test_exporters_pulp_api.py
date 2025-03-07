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

from pulpcore.client.pulpcore.api.exporters_pulp_api import ExportersPulpApi


class TestExportersPulpApi(unittest.TestCase):
    """ExportersPulpApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExportersPulpApi()

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create a pulp exporter
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete a pulp exporter
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List pulp exporters
        """
        pass

    def test_partial_update(self) -> None:
        """Test case for partial_update

        Update a pulp exporter
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Inspect a pulp exporter
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update a pulp exporter
        """
        pass


if __name__ == '__main__':
    unittest.main()
