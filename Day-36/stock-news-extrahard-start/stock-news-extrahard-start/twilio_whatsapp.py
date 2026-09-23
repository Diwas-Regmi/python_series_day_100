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
class Solution:
    def isPalindrome(self, x: int) -> bool:
        listed_x = [letter for letter in str(x)]
        reversed_x = [listed_x[i] for i in range(len(listed_x) - 1, -1, -1)]
        transformed_x = "".join(listed_x)
        transformed_reversed_x = "".join(reversed_x)
        print(listed_x)
        print(reversed_x)
        print(transformed_x)
        print(transformed_reversed_x)
        if transformed_x == transformed_reversed_x:
            return True
        else:
            return False
solution = Solution()
print(solution.isPalindrome(121))