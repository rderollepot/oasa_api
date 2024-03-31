from typing import List, Dict, Union
from pandas import DataFrame, json_normalize

from oasa_api.exceptions import OASAApiException


class Result:
    """
    This class represents the result returned from the low-level RestAdapter. It encapsulates the HTTP status code,
    a human-readable message, and the response data.
    """
    def __init__(self, status_code: int, message: str = '', data: Union[List[Dict], Dict] = None):
        """
        Initializes the Result object with the provided parameters.
        :param status_code: (int): Standard HTTP status code.
        :param message: (str, optional): Human-readable result message. Default is an empty string.
        :param data: (Union[List[Dict], Dict], optional): Response data, either a list of dictionaries or a single
        dictionary. Default is None.
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

    def parse_data(self) -> Union[Dict[str, DataFrame], DataFrame]:
        """
        Parses the response data into Pandas DataFrame(s).
        :return: (Union[Dict[str, pandas.DataFrame], pandas.DataFrame]): Parsed data as a Pandas DataFrame or dictionary of
        DataFrames.
        """
        if isinstance(self.data, List):
            return json_normalize(self.data)
        elif isinstance(self.data, Dict):
            return {k: json_normalize(v) for k, v in self.data.items()}
        else:
            raise OASAApiException("Unusual data type")
