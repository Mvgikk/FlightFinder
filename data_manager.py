import os
import requests
from dotenv import load_dotenv
load_dotenv()
sheety_prices_endpoint = os.getenv("SHEETY_PRICES_ENDPOINT")
class DataManager:
    def __init__(self):
        self.destination_data = {}

    #method for getting all data

    def get_destination_data(self):
        response = requests.get(url=sheety_prices_endpoint)
        response.raise_for_status()
        response_data = response.json()
        self.destination_data = response_data['flightDeals']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'flightDeal':{
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(
                url=f"{sheety_prices_endpoint}/{city['id']}",
                json=new_data
            )
        # print(response.text)
