import os
from twilio.rest import Client
from dotenv import load_dotenv


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
my_whatsapp_num = os.environ["MY_WHATSAPP_NUM"]
client_whatsapp_num = os.environ["CLIENT_WHATSAPP_NUM"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=my_whatsapp_num,
    from_=client_whatsapp_num,
    content_sid="HXfe5ab5f00277942d4d4200328b4d403c",
    body = "Please Brin an Umbrella"
)
print(message.sid)
print(message.status)
