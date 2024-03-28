# FlightFinder

Flight Price Tracker is a Python application designed to help users track flight prices and receive notifications when prices drop below a certain threshold.

## Features

- Retrieves flight data from Tequila Kiwi API, a flight search engine, to obtain information about available flights.
- Checks flight prices against predefined criteria using the Tequila Kiwi to determine if prices meet the defined thresholds.
- Sends SMS notifications using Twilio API to notify users about low-priced flight deals.
- Utilizes environment variables for configuration, allowing for secure storage of sensitive API keys and endpoint URLs.
- Stores price thresholds and IATA codes for cities in a Google Sheet, providing flexibility to add and update destinations using the Sheety API.
