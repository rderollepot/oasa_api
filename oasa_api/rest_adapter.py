import requests
import requests.packages
import logging
from typing import Dict
from json import JSONDecodeError
from enum import Enum

from oasa_api.models import Result
from oasa_api.exceptions import OASAApiException


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"


class RestAdapter:
    """
    This class is responsible for interacting with the OASA REST API. It handles HTTP requests (GET and POST) to the API
    endpoints and processes the responses.
    """
    def __init__(self, url: str, ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Initializes the RestAdapter object with the provided parameters.
        :param url: (str): Full path to the OASA API endpoint.
        :param ssl_verify: (bool, optional): Whether to verify SSL certificates. Default is True.
        :param logger: (logging.Logger, optional): Logger instance to use for logging. Default is None.
        """
        self._logger = logger or logging.getLogger(__name__)
        self.url = url
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: HttpMethod, params: Dict = None, data: Dict = None) -> Result:
        """
        Performs an HTTP request using the specified method, parameters, and data.
        :param http_method: (HttpMethod): The HTTP method (GET or POST) for the request.
        :param params: (Dict, optional): Parameters to include in the request URL. Default is None.
        :param data: (Dict, optional): Data to include in the request body for POST requests. Default is None.
        :return: An instance of the Result class containing the response data.
        """
        log_line_pre = f"method={http_method.value}, url={self.url}, params={params}"
        log_line_post = "success={}, status_code={}, message={}"
        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method.value, url=self.url, verify=self._ssl_verify,
                                        params=params, json=data)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise OASAApiException("Request failed") from e
        # Deserialize JSON output to Python object, or return failed Result on exception
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            self._logger.error(msg=', '.join([log_line_pre, log_line_post.format(False, None, e)]))
            raise OASAApiException("Bad JSON in response") from e
        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200
        log_line = ', '.join([log_line_pre, log_line_post.format(is_success, response.status_code, response.reason)])
        if is_success:
            self._logger.debug(msg=log_line)
            return Result(response.status_code, message=response.reason, data=data_out)
        self._logger.error(msg=log_line)
        raise OASAApiException(f"{response.status_code}: {response.reason}")

    def get(self, params: Dict = None) -> Result:
        """
        Performs a GET request to the OASA API.
        :param params: (Dict, optional): Parameters to include in the GET request URL. Default is None.
        :return: An instance of the Result class containing the response data.
        """
        return self._do(http_method=HttpMethod.GET, params=params)

    def post(self, params: Dict = None, data: Dict = None) -> Result:
        """
        Performs a POST request to the OASA API.
        :param params: (Dict, optional): Parameters to include in the POST request URL. Default is None.
        :param data: (Dict, optional): Data to include in the POST request body. Default is None.
        :return: An instance of the Result class containing the response data.
        """
        return self._do(http_method=HttpMethod.POST, params=params, data=data)
