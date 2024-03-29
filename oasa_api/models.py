from typing import List, Dict, Union
import pandas as pd

from oasa_api.exceptions import OASAApiException


class Result:
    def __init__(self, status_code: int, message: str = '', data: Union[List[Dict], Dict] = None):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

    def parse_data(self) -> Union[Dict[str, pd.DataFrame], pd.DataFrame]:
        if isinstance(self.data, List):
            return pd.json_normalize(self.data)
        elif isinstance(self.data, Dict):
            return {k: pd.json_normalize(v) for k, v in self.data.items()}
        else:
            raise OASAApiException("Unusual data type")
