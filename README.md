# OASA API Wrapper

This Python package provides a convenient wrapper for interacting with the OASA S.A. (Athens Public Transport) API,
allowing users to retrieve various information related to the public transport network in Athens, Greece.

The OASA S.A. API provides access to information such bus lines, schedules, routes, stops, arrivals, and bus locations.
The information obtained through this package corresponds to the data available on the [OASA S.A. website](https://www.oasa.gr/en/),
providing users  with a programmatic way to access the same data.

## Installation

You can install the package via pip:

```bash
pip install oasa-api
```

## Usage

To use the package, simply import the OASAApi class from the oasa_api module and create an instance of it. Then, you can
call various methods to retrieve information from the OASA API.

Here's an example of how to retrieve information about lines with master line info:

```python
from oasa_api import OASAApi

# Create an instance of OASAApi
oasa_api = OASAApi()

# Retrieve information about lines with master line info
lines_with_master_line_info = oasa_api.get_lines_with_master_line_info()

print(lines_with_master_line_info)
```

For more detailed usage examples, please refer to the [demo notebook](./demo.ipynb).

## Available Methods

- `get_master_lines()`
- `get_master_line_name(ml_code: int)`
- `get_lines_with_master_line_info()`
- `get_lines_and_routes_for_master_line_and_line_code(ml_code: int, line_code: int)`
- `get_lines()`
- `get_line_name(line_code: int)`
- `get_schedule_days_master_line(line_code: int)`
- `get_daily_schedule(line_code: int)`
- `get_sched_lines(ml_code: int, sdc_code: int, line_code: int)`
- `get_routes(line_code: int)`
- `get_routes_for_line(line_code: int)`
- `get_route_name(route_code: int)`
- `get_routes_details_and_stops(route_code: int)`
- `get_route_details(route_code: int)`
- `get_stops(route_code: int)`
- `get_routes_for_stops(stop_code: int)`
- `get_stop_name_and_xy(stop_code: int)`
- `get_closest_stops(lng: float, lat: float)`
- `get_stop_arrivals(stop_code: int)`
- `get_bus_location(route_code: int)`

For detailed information about each method, refer to the documentation in the source code.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or
submit a pull request.

## Acknowledgements

Special thanks to Pretzel for writing a
[helpful tutorial](https://www.pretzellogix.net/2021/12/08/how-to-write-a-python3-sdk-library-module-for-a-json-rest-api/)
on creating Python SDK libraries for REST APIs, and to [ChatGPT](https://chat.openai.com/)
for assisting with the documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
