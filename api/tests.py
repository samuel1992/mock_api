from django.test import TestCase

from api.models import Path, MockResponse

from api.views import endpoint_to_regex, NOT_FOUND_RESPONSE


class PathAndMockResponseNameTest(TestCase):
    def setUp(self):
        endpoint = '/test/{integer}/{string}'
        self.path = Path.objects.create(endpoint_string=endpoint,
                                        http_method='GET')
        self.mock_response = MockResponse.objects.create(body={},
                                                         status=200,
                                                         path=self.path)

    def test_path_name(self):
        self.assertEqual(str(self.path), self.path.endpoint_string)

    def test_mock_response_name(self):
        status = self.mock_response.status
        http_method = self.path.http_method
        expected_name = f'{status} -- {http_method} for {self.path}'

        self.assertEqual(str(self.mock_response), expected_name)


class ConvertEndpointToRegexTest(TestCase):
    def setUp(self):
        self.endpoint = '/test/{integer}/{string}'

    def test_convert_a_empty_endpoint_to_regex(self):
        self.assertEqual(endpoint_to_regex(''), '$')

    def test_convert_endpoint_to_regex(self):
        expected_regex = '/test/[0-9]+/[A-z]+$'

        self.assertEqual(endpoint_to_regex(self.endpoint), expected_regex)


class RouterViewTest(TestCase):
    def setUp(self):
        self.endpoint = '/test/{integer}/{string}'
        self.body = {'test': 'test test'}
        self.path = Path.objects.create(endpoint_string=self.endpoint,
                                        http_method='GET')
        self.mock_response = MockResponse.objects.create(body=self.body,
                                                         status=200,
                                                         path=self.path)

    def test_request_an_existent_mock_endpoint(self):
        endpoint = self.endpoint.replace('{integer}', '1234')
        endpoint = endpoint.replace('{string}', 'somestring')

        response = self.client.get(endpoint)

        self.assertEqual(response.status_code, self.mock_response.status)

    def test_request_an_existent_mock_endpoint_with_slash_in_the_end(self):
        endpoint = self.endpoint.replace('{integer}', '1234')
        endpoint = endpoint.replace('{string}', 'somestring')
        endpoint += '/'

        response = self.client.get(endpoint)

        self.assertEqual(response.status_code, self.mock_response.status)

    def test_request_a_existent_endpoint_but_with_different_http_method(self):
        endpoint = self.endpoint.replace('{integer}', '1234')
        endpoint = endpoint.replace('{string}', 'somestring')

        response = self.client.post(endpoint)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), NOT_FOUND_RESPONSE)

    def test_request_a_non_existent_mock_endpoint(self):
        response = self.client.get('/nonexistentendpoint')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), NOT_FOUND_RESPONSE)
