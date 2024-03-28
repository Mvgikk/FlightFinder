from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

twilio_sid = os.getenv("TWILIO_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
my_number = os.getenv("MY_NUMBER")

class NotificationManager:
    def __init__(self):

        self.client = Client(twilio_sid, twilio_auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_number,
            to=my_number,
        )
        print(message)