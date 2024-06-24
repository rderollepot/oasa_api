import pytest

from oasa_api.models import Result
from oasa_api.exceptions import OASAApiException


def test_result_parse_data_list():
    data = [{'id': '1', 'name': 'Stop 1'}, {'id': '2', 'name': 'Stop 2'}]
    result = Result(status_code=200, data=data)
    df_list = result.parse_data()

    assert len(df_list) == 2
    assert df_list.loc[0, 'id'] == '1'


def test_result_parse_data_dict():
    data = {'stops': [{'id': '1', 'name': 'Stop 1'}, {'id': '2', 'name': 'Stop 2'}]}
    result = Result(status_code=200, data=data)
    df_dict = result.parse_data()

    assert len(df_dict['stops']) == 2
    assert df_dict['stops'].loc[0, 'id'] == '1'


# noinspection PyTypeChecker
def test_result_parse_data_invalid():
    result = Result(status_code=200, data='invalid')
    with pytest.raises(OASAApiException):
        result.parse_data()
