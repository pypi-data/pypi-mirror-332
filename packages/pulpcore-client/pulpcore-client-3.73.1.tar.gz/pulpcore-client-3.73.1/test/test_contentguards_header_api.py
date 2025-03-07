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

from pulpcore.client.pulpcore.api.contentguards_header_api import ContentguardsHeaderApi


class TestContentguardsHeaderApi(unittest.TestCase):
    """ContentguardsHeaderApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContentguardsHeaderApi()

    def tearDown(self) -> None:
        pass

    def test_add_role(self) -> None:
        """Test case for add_role

        Add a role
        """
        pass

    def test_create(self) -> None:
        """Test case for create

        Create a header content guard
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete a header content guard
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List header content guards
        """
        pass

    def test_list_roles(self) -> None:
        """Test case for list_roles

        List roles
        """
        pass

    def test_my_permissions(self) -> None:
        """Test case for my_permissions

        List user permissions
        """
        pass

    def test_partial_update(self) -> None:
        """Test case for partial_update

        Update a header content guard
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Inspect a header content guard
        """
        pass

    def test_remove_role(self) -> None:
        """Test case for remove_role

        Remove a role
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update a header content guard
        """
        pass


if __name__ == '__main__':
    unittest.main()
