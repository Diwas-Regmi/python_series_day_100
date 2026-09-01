import requests
from dotenv import load_dotenv
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
import os

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def search_cheapest_flight(data,return_date):
    # Handle empty data if no flight data is returned
    if data is None or not(data.get("best_flights")) and not(data.get("other_flights")):
        print("No Flight Detected")
        return FlightData("N/A", "N/A","N/A","N/A","N/A")
    #Combine both best_flight and Other_flights
    all_flights = data.get("best_flights", []) + data.get("other_flights",[])
    first_flight= all_flights[0]
    lowest_price = first_flight["price"]
    origin = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][0]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price,origin,destination,out_date,return_date)

    for flights in all_flights:
        # Exception handling - json has data but flight is missing 'price'. Skip.
        try:
            price = flights["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price:
            lowest_price = price
            origin = flights["flights"][0]["departure_airport"]["id"]
            destination = flights["flights"][0]["arrival_airport"]["id"]
            out_date = flights["flights"][0]["departure_airport"]["time"].split(" ")[0]
            cheapest_flight = FlightData(lowest_price,origin,destination,out_date,return_date)
            print(f"Lowest price to {destination} is GBP {lowest_price}")

    return cheapest_flight








