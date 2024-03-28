import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()
ORIGIN_CITY_IATA = "WAW"



def main():
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    if sheet_data[0]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_iata_code_for_city(row["city"])
        pprint(f"sheet_data:\n {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()


    tomorrow = dt.datetime.now() + dt.timedelta(days=1)
    six_month_from_today = dt.datetime.now() + dt.timedelta(days=(6 * 30))

    for destination in sheet_data:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight.price < destination["averagePrice"]:
            notification_manager.send_sms(
                message=f"Low price alert!\n Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport},\n from {flight.out_date} to {flight.return_date}."
            )


if __name__ == "__main__":
    main()