import os
from internetspeedtwitter import InternetSpeedTwitterBot
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ['Y_EMAIL']
PASSWORD = os.environ['Y_PASSWORD']
URL = os.environ['Y_LOGIN_URL']
PROMISED_UP = os.environ['PROMISED_UP']
PROMISED_DOWN = os.environ['PROMISED_DOWN']

internet = InternetSpeedTwitterBot(URL,PASSWORD,EMAIL,PROMISED_DOWN,PROMISED_UP)