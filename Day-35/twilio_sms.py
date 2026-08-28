import os
from twilio.rest import Client
from dotenv import load_dotenv


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
my_num = os.environ["MY_NUM"]
client_num = os.environ["CLIENT_NUM"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=my_num,
    from_=client_num,
    body="sms_internal_alerts", #Trilio dont allow custom messages now a days so going with their pre installed command
)

# print(message.sid)
print(message.status)