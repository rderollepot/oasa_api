import requests
import pandas as pd


class OASAAPIClient:
    def __init__(self):
        self.base_url = "https://telematics.oasa.gr/api/"
        self.session = requests.Session()
        self.rate_limit_delay = 1  # Adjust as needed to prevent overloading the server

    def get_data(self, payload):
        response = self.session.get(self.base_url, params=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from {response.url}. Status code: {response.status_code}")
            return None

    def post_data(self, payload, data=None):
        response = self.session.post(self.base_url, params=payload, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to post data to {response.url}. Status code: {response.status_code}")
            return None

    def get_master_lines(self):
        r = self.get_data({'act': 'webGetMasterLines'})
        if r is not None:
            return pd.json_normalize(r)

    def get_master_line_name(self, ml_code):
        r = self.get_data({'act': 'getMLName', 'p1': str(ml_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_lines_with_master_line_info(self):
        r = self.get_data({'act': 'webGetLinesWithMLInfo'})
        if r is not None:
            return pd.json_normalize(r)

    def get_lines_and_routes_for_master_line_and_line_code(self, ml_code, line_code):
        # Does not seem to be implemented, always return null
        r = self.get_data({'act': 'getLinesAndRoutesForMlandLCode', 'p1': str(ml_code), 'p2': str(line_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_lines(self):
        r = self.get_data({'act': 'webGetLines'})
        if r is not None:
            return pd.json_normalize(r)

    def get_line_name(self, line_code):
        r = self.get_data({'act': 'getLineName', 'p1': str(line_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_schedule_days_master_line(self, line_code):
        r = self.get_data({'act': 'getScheduleDaysMasterline', 'p1': str(line_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_daily_schedule(self, line_code):
        r = self.get_data({'act': 'getDailySchedule', 'line_code': str(line_code)})
        if r is not None:
            come = pd.json_normalize(r['come'])
            go = pd.json_normalize(r['go'])
            return come, go

    def get_sched_lines(self, ml_code, sdc_code, line_code):
        r = self.get_data({'act': 'getSchedLines', 'p1': str(ml_code), 'p2': str(sdc_code), 'p3': str(line_code)})
        if r is not None:
            come = pd.json_normalize(r['come'])
            go = pd.json_normalize(r['go'])
            return come, go

    def get_routes(self, line_code):
        r = self.get_data({'act': 'webGetRoutes', 'p1': str(line_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_routes_for_line(self, line_code):
        r = self.get_data({'act': 'getRoutesForLine', 'p1': str(line_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_route_name(self, route_code):
        r = self.get_data({'act': 'getRouteName', 'p1': str(route_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_routes_details_and_stops(self, route_code):
        r = self.get_data({'act': 'webGetRoutesDetailsAndStops', 'p1': str(route_code)})
        if r is not None:
            details = pd.json_normalize(r['details'])
            stops = pd.json_normalize(r['stops'])
            return details, stops

    def get_route_details(self, route_code):
        r = self.get_data({'act': 'webRouteDetails', 'p1': str(route_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_stops(self, route_code):
        r = self.get_data({'act': 'webGetStops', 'p1': str(route_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_routes_for_stops(self, stop_code):
        r = self.get_data({'act': 'webRoutesForStop', 'p1': str(stop_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_stop_name_and_xy(self, stop_code):
        r = self.get_data({'act': 'getStopNameAndXY', 'p1': str(stop_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_closest_stops(self, lng, lat):
        r = self.get_data({'act': 'getClosestStops', 'p1': str(lng), 'p2': str(lat)})
        if r is not None:
            return pd.json_normalize(r)

    def get_stop_arrivals(self, stop_code):
        r = self.get_data({'act': 'getStopArrivals', 'p1': str(stop_code)})
        if r is not None:
            return pd.json_normalize(r)

    def get_bus_location(self, route_code):
        r = self.get_data({'act': 'getBusLocation', 'p1': str(route_code)})
        if r is not None:
            return pd.json_normalize(r)
