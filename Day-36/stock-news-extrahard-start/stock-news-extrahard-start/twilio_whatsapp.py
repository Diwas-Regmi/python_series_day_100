# import os
# from twilio.rest import Client
# from dotenv import load_dotenv
# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
# load_dotenv()
# sms = f"hello hi"
# account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
# my_number = os.environ["MY_WHATSAPP"]
# sender_number = os.environ["sender_whatsapp"]
#
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     to=my_number,
#     from_=sender_number,
#     body = sms,
#     content_sid="HXfe5ab5f00277942d4d4200328b4d403c",
# )
#
# print(message.status)
#
