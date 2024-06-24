import pytest

from oasa_api.exceptions import OASAApiException


def test_oasa_api_exception():
    with pytest.raises(OASAApiException):
        raise OASAApiException("An error occurred")
