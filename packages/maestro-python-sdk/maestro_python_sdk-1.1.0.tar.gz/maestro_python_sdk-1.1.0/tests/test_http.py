import base64
import unittest
from unittest.mock import patch, MagicMock

from m3_python_sdk.strategies.http import HttpStrategy


class TestHttpStrategy(unittest.TestCase):
    def setUp(self):
        self.sdk_access_key = 'De38aDdcFVA7GJ2M'
        self.sdk_secret_key = 'nBed3eFonWbQ9ecG'
        self.maestro_user = 'test_maestro_user'
        self.api_link = 'https://api.example.com'

        self.http_strategy = HttpStrategy(
            sdk_access_key=self.sdk_access_key,
            sdk_secret_key=self.sdk_secret_key,
            maestro_user=self.maestro_user,
            api_link=self.api_link
        )

    def test_initialization(self):
        self.assertEqual(self.http_strategy._sdk_access_key, self.sdk_access_key)
        self.assertEqual(self.http_strategy._sdk_secret_key, self.sdk_secret_key)
        self.assertEqual(self.http_strategy._maestro_user, self.maestro_user)
        self.assertEqual(self.http_strategy._api_link, self.api_link)

    def test_build(self):
        host = 'api.example.com'
        https = True
        port = 443
        stage = 'v1'
        built_http_strategy = HttpStrategy.build(
            host=host,
            https=https,
            port=port,
            stage=stage,
            sdk_access_key=self.sdk_access_key,
            sdk_secret_key=self.sdk_secret_key,
            maestro_user=self.maestro_user
        )
        expected_api_link = f'https://{host}:{port}/{stage}'
        self.assertEqual(built_http_strategy._api_link, expected_api_link)
        self.assertEqual(built_http_strategy._sdk_access_key, self.sdk_access_key)
        self.assertEqual(built_http_strategy._sdk_secret_key, self.sdk_secret_key)
        self.assertEqual(built_http_strategy._maestro_user, self.maestro_user)

    @patch('requests.post')
    def test_make_request(self, mock_post):
        request_data = {'key': 'value'}
        command_name = 'test_command'
        mock_response = MagicMock()
        mock_response.status_code = 200
        response_content = self.http_strategy._encrypt(
            self.sdk_secret_key,
            '{"results": [{"status": "SUCCESS", "data": "Test data"}]}'
        )
        mock_response.content = response_content
        mock_post.return_value = mock_response

        response = self.http_strategy.make_request(request_data, command_name)
        self.assertEqual(
            response,
            {'message': 'Test data', 'status': 'SUCCESS', 'status_code': None}
        )

    @patch('requests.post')
    def test_make_request_with_error(self, mock_post):
        request_data = {'key': 'value'}
        command_name = 'test_command'
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raw.reason = 'Not Found'
        mock_post.return_value = mock_response

        with self.assertRaises(Exception) as context:
            self.http_strategy.make_request(request_data, command_name)
        self.assertIn('Requested resource not found', str(context.exception))

    @patch('requests.post')
    def test_make_request_unauthorized(self, mock_post):
        request_data = {'key': 'value'}
        command_name = 'test_command'
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_post.return_value = mock_response

        with self.assertRaises(Exception) as context:
            self.http_strategy.make_request(request_data, command_name)
        self.assertIn('Bad Credentials', str(context.exception))


if __name__ == '__main__':
    unittest.main()
