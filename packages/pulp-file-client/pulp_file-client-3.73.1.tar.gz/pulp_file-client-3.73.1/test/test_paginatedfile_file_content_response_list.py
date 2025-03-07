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

from pulpcore.client.pulp_file.models.paginatedfile_file_content_response_list import PaginatedfileFileContentResponseList

class TestPaginatedfileFileContentResponseList(unittest.TestCase):
    """PaginatedfileFileContentResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedfileFileContentResponseList:
        """Test PaginatedfileFileContentResponseList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedfileFileContentResponseList`
        """
        model = PaginatedfileFileContentResponseList()
        if include_optional:
            return PaginatedfileFileContentResponseList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    pulpcore.client.pulp_file.models.file/file_content_response.file.FileContentResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_labels = {
                            'key' : ''
                            }, 
                        artifact = '', 
                        relative_path = '', 
                        md5 = '', 
                        sha1 = '', 
                        sha224 = '', 
                        sha256 = '', 
                        sha384 = '', 
                        sha512 = '', )
                    ]
            )
        else:
            return PaginatedfileFileContentResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulp_file.models.file/file_content_response.file.FileContentResponse(
                        pulp_href = '', 
                        prn = '', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_labels = {
                            'key' : ''
                            }, 
                        artifact = '', 
                        relative_path = '', 
                        md5 = '', 
                        sha1 = '', 
                        sha224 = '', 
                        sha256 = '', 
                        sha384 = '', 
                        sha512 = '', )
                    ],
        )
        """

    def testPaginatedfileFileContentResponseList(self):
        """Test PaginatedfileFileContentResponseList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
