import pytest
from unittest.mock import patch, Mock
from requests.exceptions import RequestException

from oasa_api.rest_adapter import RestAdapter, HttpMethod
from oasa_api.exceptions import OASAApiException


@patch('oasa_api.rest_adapter.requests.request')
def test_get_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'data': 'value'}
    mock_get.return_value = mock_response

    adapter = RestAdapter('https://fakeurl.com')
    result = adapter.get(params={'param1': 'value1'})

    assert result.data['data'] == 'value'


@patch('oasa_api.rest_adapter.requests.request')
def test_do_get_success(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'data': 'value'}
    mock_request.return_value = mock_response

    adapter = RestAdapter('https://fakeurl.com')
    result = adapter._do(http_method=HttpMethod.GET, params={'param1': 'value1'})

    assert result.data['data'] == 'value'


@patch('oasa_api.rest_adapter.requests.request')
def test_do_post_success(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'data': 'value'}
    mock_request.return_value = mock_response

    adapter = RestAdapter('https://fakeurl.com')
    result = adapter._do(http_method=HttpMethod.POST, params={'param1': 'value1'}, data={'key': 'value'})

    assert result.data['data'] == 'value'


@patch('oasa_api.rest_adapter.requests.request')
def test_do_request_failure(mock_request):
    mock_request.side_effect = RequestException()

    adapter = RestAdapter('https://fakeurl.com')
    with pytest.raises(OASAApiException):
        adapter._do(http_method=HttpMethod.GET)


@patch('oasa_api.rest_adapter.requests.request')
def test_do_json_failure(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError()
    mock_request.return_value = mock_response

    adapter = RestAdapter('https://fakeurl.com')
    with pytest.raises(OASAApiException):
        adapter._do(http_method=HttpMethod.GET)


@patch('oasa_api.rest_adapter.requests.request')
def test_do_status_code_failure(mock_request):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {'data': 'value'}
    mock_request.return_value = mock_response

    adapter = RestAdapter('https://fakeurl.com')
    with pytest.raises(OASAApiException):
        adapter._do(http_method=HttpMethod.GET)
