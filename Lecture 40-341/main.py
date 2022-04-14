from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

import requests

POST_ENDPOINT = "https://api.sheety.co/64f8853f70e41423e6373e05ac5044e1/flightDeals/users"

first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()

while True:
    email = input("What is your email address?\n").lower()
    email_val = input("Please re-enter your email.\n").lower()
    if email != email_val:
        print("Emails do not match, please re enter ")
    else:
        data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }

        response = requests.post(url=POST_ENDPOINT, json=data)
        print("You are in the club!")

    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    ORIGIN_CITY_IATA = "BAK"

    if sheet_data[0]["iataCode"] == "":
        city_names = [row["city"] for row in sheet_data]
        data_manager.city_codes = flight_search.get_destination_codes(city_names)
        data_manager.update_destination_codes()
        sheet_data = data_manager.get_destination_data()

    destinations = {
        data["iataCode"]: {
            "id": data["id"],
            "city": data["city"],
            "price": data["lowestPrice"]
        } for data in sheet_data}

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination_code in destinations:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination_code,
            from_time=tomorrow,
            to_time=six_month_from_today
        )

        if flight is None:
            continue

        if flight.price < destinations[destination_code]["price"]:
            users = data_manager.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]

            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                      f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} " \
                      f"to {flight.return_date}."

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
                   f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

            notification_manager.send_emails(emails, message, link)
