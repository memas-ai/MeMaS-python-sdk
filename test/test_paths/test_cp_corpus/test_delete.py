# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import memas_sdk
from memas_sdk.paths.cp_corpus import delete  # noqa: E501
from memas_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCpCorpus(ApiTestMixin, unittest.TestCase):
    """
    CpCorpus unit test stubs
        Delete corpus  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
