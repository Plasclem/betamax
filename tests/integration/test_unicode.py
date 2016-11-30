from betamax import Betamax
from tests.integration.helper import IntegrationHelper
from betamax.mock_response import MockHTTPResponse
from requests.packages.urllib3._collections import HTTPHeaderDict
import unittest


class TestUnicode(IntegrationHelper):
    def test_unicode_is_saved_properly(self):
        s = self.session
        # https://github.com/kanzure/python-requestions/issues/4
        url = 'http://www.amazon.com/review/RAYTXRF3122TO'

        with Betamax(s).use_cassette('test_unicode') as beta:
            self.cassette_path = beta.current_cassette.cassette_path
            s.get(url)


class TestMockUnicode(unittest.TestCase):
    """
    Unittest to showcase the behaviour of MockHTTPResponse with headers containing LATIN1 encoded characters,
    especially in filenames.
    """

    def test_mock_response_with_unicode(self):
        headers = HTTPHeaderDict({'Content-Disposition': 'attachment; filename="\xe9";'})
        MockHTTPResponse(headers)
