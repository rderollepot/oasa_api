import logging
from typing import Dict
from pandas import DataFrame

from oasa_api.rest_adapter import RestAdapter


class OASAApi:
    """
    This class serves as a high-level interface for interacting with the OASA API. It encapsulates methods for
    retrieving various information related to public transportation in Athens.
    """
    def __init__(self, ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Initializes the OASAApi object with the provided parameters.
        :param ssl_verify: (bool, optional): Whether to verify SSL certificates. Default is True.
        :param logger: (logging.Logger, optional): Logger instance to use for logging. Default is None.
        """
        self._rest_adapter = RestAdapter("https://telematics.oasa.gr/api/", ssl_verify, logger)

    def get_master_lines(self) -> DataFrame:
        """
        Retrieves information about master lines from the OASA API.
        :return: Information about master lines.
        """
        result = self._rest_adapter.get(params={'act': 'webGetMasterLines'})
        return result.parse_data()

    def get_master_line_name(self, ml_code: int) -> DataFrame:
        """
        Retrieves the name of a master line associated with the specified ml_code.
        :param ml_code: (int): The code of the master line.
        :return: Information about the master line name.
        """
        result = self._rest_adapter.get(params={'act': 'getMLName', 'p1': str(ml_code)})
        return result.parse_data()

    def get_lines_with_master_line_info(self) -> DataFrame:
        """
        Retrieves information about lines with associated master line from the OASA API.
        :return: Information about lines with associated master line.
        """
        result = self._rest_adapter.get(params={'act': 'webGetLinesWithMLInfo'})
        return result.parse_data()

    def get_lines_and_routes_for_master_line_and_line_code(self, ml_code: int, line_code: int) -> DataFrame:
        """
        Retrieves information about lines and routes for a specific master line and line code from the OASA API. (Does
        not seem to be implemented, always return null...)
        :param ml_code: (int): The code of the master line.
        :param line_code: (int): The code of the line.
        :return: Information about lines and routes.
        """
        result = self._rest_adapter.get(params={'act': 'getLinesAndRoutesForMlandLCode', 'p1': str(ml_code),
                                                'p2': str(line_code)})
        return result.parse_data()

    def get_lines(self) -> DataFrame:
        """
        Retrieves information about lines from the OASA API.
        :return: Information about lines.
        """
        result = self._rest_adapter.get(params={'act': 'webGetLines'})
        return result.parse_data()

    def get_line_name(self, line_code: int) -> DataFrame:
        """
        Retrieves the name of a line associated with the specified line_code.
        :param line_code: (int): The code of the line.
        :return: Information about the line name.
        """
        result = self._rest_adapter.get(params={'act': 'getLineName', 'p1': str(line_code)})
        return result.parse_data()

    def get_schedule_days_master_line(self, line_code: int) -> DataFrame:
        """
        Retrieves information about the schedule days for the specified line code from the OASA API.
        :param line_code: (int): The code of the line.
        :return: Information about the schedule days for the master line.
        """
        result = self._rest_adapter.get(params={'act': 'getScheduleDaysMasterline', 'p1': str(line_code)})
        return result.parse_data()

    def get_daily_schedule(self, line_code: int) -> Dict[str, DataFrame]:
        """
        Retrieves information about the daily schedule for the specified line code from the OASA API.
        :param line_code: (int): The code of the line.
        :return: Information about the daily schedule for the line.
        """
        result = self._rest_adapter.get(params={'act': 'getDailySchedule', 'line_code': str(line_code)})
        return result.parse_data()

    def get_schedule_lines(self, ml_code: int, sdc_code: int, line_code: int) -> Dict[str, DataFrame]:
        """
        Retrieves information about scheduled lines for the specified master line, schedule day code, and line code from
        the OASA API.
        :param ml_code: (int): The code of the master line.
        :param sdc_code: (int): The schedule day code.
        :param line_code: (int): The code of the line.
        :return: Information about scheduled lines.
        """
        result = self._rest_adapter.get(params={'act': 'getSchedLines', 'p1': str(ml_code),
                                                'p2': str(sdc_code), 'p3': str(line_code)})
        return result.parse_data()

    def get_routes(self, line_code: int) -> DataFrame:
        """
        Retrieves information about routes for the specified line code from the OASA API.
        :param line_code: (int): The code of the line.
        :return: Information about routes for the line.
        """
        result = self._rest_adapter.get(params={'act': 'webGetRoutes', 'p1': str(line_code)})
        return result.parse_data()

    def get_routes_for_line(self, line_code: int) -> DataFrame:
        """
        Retrieves information about routes for the specified line code from the OASA API.
        :param line_code: (int): The code of the line.
        :return: Information about routes for the line.
        """
        result = self._rest_adapter.get(params={'act': 'getRoutesForLine', 'p1': str(line_code)})
        return result.parse_data()

    def get_route_name(self, route_code: int) -> DataFrame:
        """
        Retrieves the name of the route associated with the specified route code from the OASA API.
        :param route_code: (int): The code of the route.
        :return: Information about the name of the route.
        """
        result = self._rest_adapter.get(params={'act': 'getRouteName', 'p1': str(route_code)})
        return result.parse_data()

    def get_routes_details_and_stops(self, route_code: int) -> Dict[str, DataFrame]:
        """
        Retrieves information about route details and stops for the specified route code from the OASA API.
        :param route_code: (int): The code of the route.
        :return: Information about route details and stops.
        """
        result = self._rest_adapter.get(params={'act': 'webGetRoutesDetailsAndStops', 'p1': str(route_code)})
        return result.parse_data()

    def get_route_details(self, route_code: int) -> DataFrame:
        """
        Retrieves detailed information about the specified route code from the OASA API.
        :param route_code: (int): The code of the route.
        :return: Information about route details.
        """
        result = self._rest_adapter.get(params={'act': 'webRouteDetails', 'p1': str(route_code)})
        return result.parse_data()

    def get_stops(self, route_code: int) -> DataFrame:
        """
        Retrieves information about stops for the specified route code from the OASA API.
        :param route_code: (int): The code of the route.
        :return: Information about stops for the route.
        """
        result = self._rest_adapter.get(params={'act': 'webGetStops', 'p1': str(route_code)})
        return result.parse_data()

    def get_routes_for_stop(self, stop_code: int) -> DataFrame:
        """
        Retrieves information about routes associated with the specified stop code from the OASA API.
        :param stop_code: (int): The code of the stop.
        :return: Information about routes for the stop.
        """
        result = self._rest_adapter.get(params={'act': 'webRoutesForStop', 'p1': str(stop_code)})
        return result.parse_data()

    def get_stop_name_and_xy(self, stop_code: int) -> DataFrame:
        """
        Retrieves the name and XY coordinates of the stop associated with the specified stop code from the OASA API.
        :param stop_code: (int): The code of the stop.
        :return: Information about the name and XY coordinates of the stop.
        """
        result = self._rest_adapter.get(params={'act': 'getStopNameAndXY', 'p1': str(stop_code)})
        return result.parse_data()

    def get_closest_stops(self, lng: float, lat: float) -> DataFrame:
        """
        Retrieves information about the closest stops to the specified longitude and latitude location from the OASA
        API.
        :param lng: (float): Longitude of the location.
        :param lat: (float): Latitude of the location.
        :return: Information about the closest stops to the specified location.
        """
        result = self._rest_adapter.get(params={'act': 'getClosestStops', 'p1': str(lng), 'p2': str(lat)})
        return result.parse_data()

    def get_stop_arrivals(self, stop_code: int) -> DataFrame:
        """
        Retrieves information about bus arrivals at the specified stop code from the OASA API.
        :param stop_code: (int): The code of the stop.
        :return: Information about bus arrivals at the stop.
        """
        result = self._rest_adapter.get(params={'act': 'getStopArrivals', 'p1': str(stop_code)})
        return result.parse_data()

    def get_bus_location(self, route_code: int) -> DataFrame:
        """
        Retrieves information about the location of the buses associated with the specified route code from the OASA
        API.
        :param route_code: (int): The code of the route.
        :return: Information about the location of the bus for the route.
        """
        result = self._rest_adapter.get(params={'act': 'getBusLocation', 'p1': str(route_code)})
        return result.parse_data()
