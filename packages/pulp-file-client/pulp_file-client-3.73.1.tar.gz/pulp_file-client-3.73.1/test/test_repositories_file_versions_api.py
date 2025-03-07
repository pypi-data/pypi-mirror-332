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

from pulpcore.client.pulp_file.api.repositories_file_versions_api import RepositoriesFileVersionsApi


class TestRepositoriesFileVersionsApi(unittest.TestCase):
    """RepositoriesFileVersionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RepositoriesFileVersionsApi()

    def tearDown(self) -> None:
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete a repository version
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List repository versions
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Inspect a repository version
        """
        pass

    def test_repair(self) -> None:
        """Test case for repair

        """
        pass


if __name__ == '__main__':
    unittest.main()
