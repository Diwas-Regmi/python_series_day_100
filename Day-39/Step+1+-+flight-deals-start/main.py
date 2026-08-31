import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight


# ==================== Conserve requests and preserve your free plan ====================
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)
# ==================== Talk to Sheety ====================
data_manager = DataManager()
sheet_data = data_manager.flight_price()
pprint(sheet_data)
# ==================== Set the Dates ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
# ==================== Do a Flight Search ====================
flight_search = FlightSearch()
flights = flight_search.check_flight(
    original_city_code="LHR",
    destination_city_code="CDG",
    from_time=tomorrow,
    to_time=six_month_from_today
)
# pprint(flights)

# ==================== Show the Cheapest Flight ====================

cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]["lowestPrice"]:
    pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
    data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price)