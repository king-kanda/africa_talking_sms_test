# import package
import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("AT_USERNAME")    # use 'sandbox' for development in the test environment
api_key = os.getenv("AT_API_KEY")

africastalking.initialize(username.strip(), api_key.strip())
sms = africastalking.SMS

if __name__ == "__main__":
    # Use the service synchronously
    response = sms.send("Hello Message! bitaa is mumhome", ["+254759626677"], sender_id="56236")
    print(response)