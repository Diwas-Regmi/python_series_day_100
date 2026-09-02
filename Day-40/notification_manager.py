import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
# sms = f"hello hi"
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
my_number = os.environ["MY_WHATSAPP"]
sender_number = os.environ["sender_whatsapp"]

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)


    def send_message(self,sms):

        message = self.client.messages.create(
            to=my_number,
            from_=sender_number,
            body=sms,
            content_sid="HXfe5ab5f00277942d4d4200328b4d403c",
        )
        print(message.status)


