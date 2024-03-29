import logging
from oasa_api.rest_adapter import RestAdapter


class OASAApi:
    def __init__(self, hostname: str = "telematics.oasa.gr", ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, ssl_verify, logger)

    def get_master_lines(self):
        result = self._rest_adapter.get(params={'act': 'webGetMasterLines'})
        return result.parse_data()

    def get_master_line_name(self, ml_code):
        result = self._rest_adapter.get(params={'act': 'getMLName', 'p1': str(ml_code)})
        return result.parse_data()

    def get_lines_with_master_line_info(self):
        result = self._rest_adapter.get(params={'act': 'webGetLinesWithMLInfo'})
        return result.parse_data()

    def get_lines_and_routes_for_master_line_and_line_code(self, ml_code, line_code):
        # Does not seem to be implemented, always return null
        result = self._rest_adapter.get(params={'act': 'getLinesAndRoutesForMlandLCode', 'p1': str(ml_code),
                                                'p2': str(line_code)})
        return result.parse_data()

    def get_lines(self):
        result = self._rest_adapter.get(params={'act': 'webGetLines'})
        return result.parse_data()

    def get_line_name(self, line_code):
        result = self._rest_adapter.get(params={'act': 'getLineName', 'p1': str(line_code)})
        return result.parse_data()

    def get_schedule_days_master_line(self, line_code):
        result = self._rest_adapter.get(params={'act': 'getScheduleDaysMasterline', 'p1': str(line_code)})
        return result.parse_data()

    def get_daily_schedule(self, line_code):
        result = self._rest_adapter.get(params={'act': 'getDailySchedule', 'line_code': str(line_code)})
        return result.parse_data()

    def get_sched_lines(self, ml_code, sdc_code, line_code):
        result = self._rest_adapter.get(params={'act': 'getSchedLines', 'p1': str(ml_code),
                                                'p2': str(sdc_code), 'p3': str(line_code)})
        return result.parse_data()

    def get_routes(self, line_code):
        result = self._rest_adapter.get(params={'act': 'webGetRoutes', 'p1': str(line_code)})
        return result.parse_data()

    def get_routes_for_line(self, line_code):
        result = self._rest_adapter.get(params={'act': 'getRoutesForLine', 'p1': str(line_code)})
        return result.parse_data()

    def get_route_name(self, route_code):
        result = self._rest_adapter.get(params={'act': 'getRouteName', 'p1': str(route_code)})
        return result.parse_data()

    def get_routes_details_and_stops(self, route_code):
        result = self._rest_adapter.get(params={'act': 'webGetRoutesDetailsAndStops', 'p1': str(route_code)})
        return result.parse_data()

    def get_route_details(self, route_code):
        result = self._rest_adapter.get(params={'act': 'webRouteDetails', 'p1': str(route_code)})
        return result.parse_data()

    def get_stops(self, route_code):
        result = self._rest_adapter.get(params={'act': 'webGetStops', 'p1': str(route_code)})
        return result.parse_data()

    def get_routes_for_stops(self, stop_code):
        result = self._rest_adapter.get(params={'act': 'webRoutesForStop', 'p1': str(stop_code)})
        return result.parse_data()

    def get_stop_name_and_xy(self, stop_code):
        result = self._rest_adapter.get(params={'act': 'getStopNameAndXY', 'p1': str(stop_code)})
        return result.parse_data()

    def get_closest_stops(self, lng, lat):
        result = self._rest_adapter.get(params={'act': 'getClosestStops', 'p1': str(lng), 'p2': str(lat)})
        return result.parse_data()

    def get_stop_arrivals(self, stop_code):
        result = self._rest_adapter.get(params={'act': 'getStopArrivals', 'p1': str(stop_code)})
        return result.parse_data()

    def get_bus_location(self, route_code):
        result = self._rest_adapter.get(params={'act': 'getBusLocation', 'p1': str(route_code)})
        return result.parse_data()
