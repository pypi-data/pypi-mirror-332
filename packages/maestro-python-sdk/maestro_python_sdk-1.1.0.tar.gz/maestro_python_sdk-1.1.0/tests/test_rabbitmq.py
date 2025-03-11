import base64
import gzip
import json
import secrets
import unittest
from unittest.mock import patch, MagicMock, ANY
import pika
import pika.exceptions

from m3_python_sdk.strategies.rabbitmq import RabbitMqStrategy
from m3_python_sdk.strategies.abstract_strategy import AbstractStrategy


class MockChannel:
    def __init__(self):
        self.consume_queue = None
        self.is_consuming = False
        self.consumer_tag = None
        self.on_message_callback = None

    def basic_consume(self, queue, on_message_callback, consumer_tag):
        self.consume_queue = queue
        self.consumer_tag = consumer_tag
        self.on_message_callback = on_message_callback
        return True

    def start_consuming(self):
        self.is_consuming = True
        self.on_message_callback(
            self,
            MagicMock(),
            MagicMock(correlation_id=self.consumer_tag),
            b'encrypted_message'
        )

    def stop_consuming(self):
        self.is_consuming = False

    def basic_ack(self, delivery_tag):
        pass

    def basic_nack(self, delivery_tag, requeue):
        pass


class TestRabbitMqStrategy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.connection_url = 'amqps://user:pass@localhost:5671'
        cls.request_queue = 'test_request_queue'
        cls.response_queue = 'test_response_queue'
        cls.rabbit_exchange = 'test_exchange'
        cls.sdk_access_key = 'test_De38aDdcFVA7'
        cls.sdk_secret_key = 'nBed3eFonWbQ9ecG' # This is a test value
        cls.maestro_user = 'test_maestro_user'
        cls.correlation_id = '1234567890'
        cls.timeout = 30
        cls.rabbit_mq_strategy = RabbitMqStrategy(
            connection_url=cls.connection_url,
            request_queue=cls.request_queue,
            response_queue=cls.response_queue,
            rabbit_exchange=cls.rabbit_exchange,
            sdk_access_key=cls.sdk_access_key,
            sdk_secret_key=cls.sdk_secret_key,
            maestro_user=cls.maestro_user,
            timeout=cls.timeout,
        )
        cls.rabbit_mq_strategy.responses = {}

    @patch('pika.BlockingConnection')
    def test_open_channel_success(self, mock_blocking_connection):
        mock_channel = MagicMock()
        mock_connection = MagicMock()
        mock_connection.channel.return_value = mock_channel
        mock_blocking_connection.return_value = mock_connection
        channel = self.rabbit_mq_strategy._open_channel()
        self.assertEqual(channel, mock_channel)
        mock_blocking_connection.assert_called_once_with(
            pika.URLParameters(self.connection_url)
        )
        mock_connection.channel.assert_called_once()

    @patch('pika.BlockingConnection')
    def test_open_channel_failure(self, mock_blocking_connection):
        mock_blocking_connection.side_effect = \
            pika.exceptions.AMQPConnectionError("Connection error")
        with self.assertRaisesRegex(Exception, 'Connection to RabbitMQ refused'):
            self.rabbit_mq_strategy._open_channel()
        mock_blocking_connection.assert_called_once_with(
            pika.URLParameters(self.connection_url))

    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._open_channel')
    def test_publish(self, mock_open_channel):
        mock_channel = MagicMock()
        mock_open_channel.return_value = mock_channel
        self.rabbit_mq_strategy.publish(
            message='test_message',
            routing_key=self.request_queue,
            exchange=self.rabbit_exchange,
        )
        mock_open_channel.assert_called_once()
        mock_channel.confirm_delivery.assert_called_once()
        mock_channel.basic_publish.assert_called_once()

    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy.publish_sync')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy.consume_sync')
    def test_execute_sync(self, mock_consume_sync, mock_publish_sync):
        mock_consume_sync.return_value = AbstractStrategy._encrypt(
            "nBed3eFonWbQ9ecG", '{"results": [{"status": "success"}]}'
        )
        raw_secret_key = secrets.token_bytes(16)
        encoded_secret_key = base64.b64encode(raw_secret_key).decode('utf-8')
        result = self.rabbit_mq_strategy.execute_sync(
            command_name='test_command',
            parameters={'param': encoded_secret_key},
            secure_parameters={'param': encoded_secret_key}
        )
        mock_publish_sync.assert_called_once()
        mock_consume_sync.assert_called_once()
        self.assertEqual(
            result, {'status_code': None, 'status': 'success', 'message': None}
        )

    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._open_channel')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._close')
    @patch('pika.BlockingConnection')
    def test_consume_sync(
            self, mock_blocking_connection, mock_close, mock_open_channel,
    ):
        # Mock the channel and connection
        mock_channel = MockChannel()
        mock_open_channel.return_value = mock_channel
        # Create a mock connection object with a `call_later` method
        mock_connection = MagicMock()
        mock_connection.call_later = MagicMock()
        mock_blocking_connection.return_value = mock_connection
        # Set the connection object to the strategy
        self.rabbit_mq_strategy.conn = mock_connection
        # Call the method under test
        result = self.rabbit_mq_strategy.consume_sync(
            queue=self.response_queue,
            correlation_id=self.correlation_id,
        )
        # Assertions
        mock_open_channel.assert_called_once()
        mock_close.assert_called_once()
        self.assertEqual(result, b'encrypted_message')
        mock_connection.call_later.assert_called_once_with(self.timeout, ANY)

    def test_build_success(self):
        strategy = RabbitMqStrategy.build(
            host='localhost',
            port=5671,
            username='user',
            password='pass',
            request_queue=self.request_queue,
            response_queue=self.response_queue,
            rabbit_exchange=self.rabbit_exchange,
            sdk_access_key=self.sdk_access_key,
            sdk_secret_key=self.sdk_secret_key,
            maestro_user=self.maestro_user,
            timeout=self.timeout,
            stage='dev',
        )
        expected_url = f'amqps://user:pass@localhost:5671/dev'
        self.assertEqual(strategy.connection_url, expected_url)
        self.assertEqual(strategy.request_queue, self.request_queue)
        self.assertEqual(strategy.response_queue, self.response_queue)

    def test_build_without_port(self):
        strategy = RabbitMqStrategy.build(
            host='localhost',
            username='user',
            password='pass',
            amqps=False,
            stage='dev',
            sdk_access_key=self.sdk_access_key,
            sdk_secret_key=self.sdk_secret_key,
            maestro_user=self.maestro_user,
        )
        expected_url = f'amqp://user:pass@localhost/dev'
        self.assertEqual(strategy.connection_url, expected_url)

    def test_request_queue_getter_setter(self):
        strategy = RabbitMqStrategy(
            connection_url='amqps://localhost',
            sdk_access_key=self.sdk_access_key,
            sdk_secret_key=self.sdk_secret_key,
            maestro_user=self.maestro_user,
            request_queue=self.request_queue,
        )
        strategy.request_queue = 'new_request_queue'
        self.assertEqual(strategy.request_queue, 'new_request_queue')

    def test_response_queue_getter_setter(self):
        strategy = RabbitMqStrategy(
            connection_url='amqps://localhost',
            sdk_access_key=self.sdk_access_key,
            sdk_secret_key=self.sdk_secret_key,
            maestro_user=self.maestro_user,
            request_queue=self.request_queue,
        )
        strategy.response_queue = 'new_response_queue'
        self.assertEqual(strategy.response_queue, 'new_response_queue')

    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._open_channel')
    def test_declare_queue(self, mock_open_channel):
        mock_channel = MagicMock()
        mock_open_channel.return_value = mock_channel
        self.rabbit_mq_strategy.declare_queue('test_queue')
        mock_channel.queue_declare \
            .assert_called_once_with(queue='test_queue', durable=True)

    def test_build_payload_flat_request(self):
        result = self.rabbit_mq_strategy \
            ._build_payload('123', 'test_command', {'param1': 'value1'}, True)
        expected = [{
            'id': '123',
            'type': None,
            'params': {'param1': 'value1', 'type': 'test_command'},
        }]
        self.assertEqual(result, expected)

    def test_build_payload_non_flat_request(self):
        result = self.rabbit_mq_strategy \
            ._build_payload('123', 'test_command', {'param1': 'value1'}, False)
        expected = [{
            'id': '123',
            'type': 'test_command',
            'params': {'param1': 'value1'},
        }]
        self.assertEqual(result, expected)

    def test_build_message_compressed(self):
        parameters = {'param1': 'value1'}
        compressed_message = self.rabbit_mq_strategy \
            ._build_message('123', 'test_command', parameters, compressed=True)
        expected_json = json.dumps([{
            'id': '123', 'type': 'test_command', 'params': parameters}
        ])
        expected_compressed = base64\
            .b64encode(gzip.compress(expected_json.encode('UTF-8'))).decode()
        self.assertEqual(compressed_message, expected_compressed)

    def test_build_secure_message(self):
        parameters = {'param1': 'value1', 'password': 'secret'}
        secure_parameters = ['password']
        result = self.rabbit_mq_strategy._build_secure_message(
            '123', 'test_command', parameters, secure_parameters
        )
        expected = [{
            'id': '123',
            'type': 'test_command',
            'params': {'param1': 'value1', 'password': '*****'}
        }]
        self.assertEqual(result, expected)

    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._build_message')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._build_secure_message')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._encrypt')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._get_signed_headers')
    def test_pre_process_request(
            self,
            mock_get_signed_headers,
            mock_encrypt,
            mock_build_secure_message,
            mock_build_message,
    ):
        # Set return values here
        mock_build_message.return_value = 'message'
        mock_build_secure_message.return_value = 'secure_message'
        mock_encrypt.return_value = 'encrypted_message'
        mock_get_signed_headers.return_value = {'header': 'value'}
        # Call the method under test
        encrypted_body, headers = self.rabbit_mq_strategy.pre_process_request(
            'test_command',
            {'param1': 'value1'},
            ['password'],
            False,
            False,
        )
        # Assert that each mock was called once
        mock_build_message.assert_called_once()
        mock_build_secure_message.assert_called_once()
        mock_encrypt.assert_called_once()
        mock_get_signed_headers.assert_called_once()
        # Assert that the return values are as expected
        self.assertEqual(encrypted_body, 'encrypted_message')
        self.assertEqual(headers, {'header': 'value'})

    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._build_request')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._build_secure_request')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._encrypt')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy._get_signed_headers')
    def test_pre_process_batch_request(
            self,
            mock_get_signed_headers,
            mock_encrypt,
            mock_build_secure_request,
            mock_build_request,
    ):
        mock_build_request.return_value = 'payload'
        mock_build_secure_request.return_value = 'secure_payload'
        mock_encrypt.return_value = 'encrypted_body'
        mock_get_signed_headers.return_value = {'header': 'value'}
        encrypted_body, headers = self.rabbit_mq_strategy.pre_process_batch_request(
            'test_command',
            {'param1': 'value1'},
            {'password': '*****'},
            False,
            False,
            False,
        )
        mock_build_request.assert_called_once()
        mock_build_secure_request.assert_called_once()
        mock_encrypt.assert_called_once()
        mock_get_signed_headers.assert_called_once()
        self.assertEqual(encrypted_body, 'encrypted_body')
        self.assertEqual(headers, {'header': 'value'})

    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy.publish_sync')
    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy.consume_sync')
    def test_execute_batch_sync(self, mock_consume_sync, mock_publish_sync):
        encrypted_response = self.rabbit_mq_strategy._encrypt(
            secret_key=self.sdk_secret_key,
            data=json.dumps({'results': [{'status': 'success'}]})
        )
        mock_consume_sync.return_value = encrypted_response
        result = self.rabbit_mq_strategy.execute_batch_sync(
            'test_command',
            [{'param1': 'value1'}],
            [{'password': '*****'}],
            False,
            False,
        )
        mock_publish_sync.assert_called_once()
        mock_consume_sync.assert_called_once()
        self.assertEqual(
            result, [{'message': None, 'status': 'success', 'status_code': None}]
        )

    @patch('m3_python_sdk.strategies.rabbitmq.RabbitMqStrategy.execute_batch_async')
    def test_execute_batch_async(self, mock_execute_batch_async):
        # Setup the mock for the async execution path
        mock_execute_batch_async.return_value = [{
            'status': 'success', 'status_code': None, 'message': None,
        }]
        # Execute the method under test
        result = self.rabbit_mq_strategy.execute_batch(
            request_data=[{'param1': 'value1'}],
            command_name='test_command',
            sync=False  # Important to set sync to False to test the async path
        )
        # Assertions to verify the correct behavior
        mock_execute_batch_async.assert_called_once_with(
            command_name='test_command',
            parameters=[{'param1': 'value1'}],
            compressed=None,
            secure_parameters=None,
            is_flat_request=None,
        )
        self.assertEqual(
            result, [{'status': 'success', 'status_code': None, 'message': None}]
        )


if __name__ == '__main__':
    unittest.main()
