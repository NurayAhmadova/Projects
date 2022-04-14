from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "BAK"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA, destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.telegram_bot_sendtext(
            bot_message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-"
                        f"{flight.origin_airport} "f"to {flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} "f"to {flight.return_date}.")