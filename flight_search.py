import requests
import os
from flight_data import FlightData
from dotenv import load_dotenv
load_dotenv()
kiwi_endpoint = os.getenv("KIWI_ENDPOINT")
kiwi_api_key = os.getenv("KIWI_API_KEY")

class FlightSearch:

    # get iata code for city name and return it
    def get_iata_code_for_city(self,city_name : str):
        header = {
            'apikey':kiwi_endpoint
        }
        params = {
            'term':city_name,
            'location_types':'airport',

        }
        response = requests.get(url=f"{kiwi_endpoint}/locations/query",params=params,headers=header)
        data = response.json()
        code = data['locations'][0]['city']['code']
        return code



    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {
            'apikey': kiwi_api_key
        }
        query = {
            'fly_from': origin_city_code,
            'date_from': from_time.strftime("%d/%m/%Y"),
            'date_to': to_time.strftime("%d/%m/%Y"),
            'fly_to': destination_city_code,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'one_for_city':1,
            'max_stopovers': 0,
            'curr': 'USD'
        }
        response = requests.get(url=f"{kiwi_endpoint}/v2/search",headers=header,params=query)
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No flights found for {destination_city_code}.')
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            out_date=data['route'][0]['local_departure'].split("T")[0],
            return_date=data['route'][1]['local_departure'].split("T")[0],
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data