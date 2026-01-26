# Twilio SMS Demo - Direct HTTP Request (without SDK)
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Your Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")

# Twilio Messages API endpoint
url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"

# Request headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Debug info (without exposing full credentials)
print(f"Account SID: {account_sid[:8]}...{account_sid[-4:]}")
print(f"From Number: {twilio_phone_number}")
print()

# Request payload (form-encoded data)
payload = {
    "To": "+1234567890",  # Replace with recipient number in E.164 format
    "From": twilio_phone_number,
    "Body": "Hello! This is a test message from Twilio API (direct HTTP request)."
}

# Make the request
print("Sending SMS request...")
print(f"Endpoint: {url}")
print(f"Payload: To={payload['To']}, From={payload['From']}, Body=...")
print()

# Send request with Basic Auth (Account SID : Auth Token)
response = requests.post(
    url,
    headers=headers,
    data=payload,
    auth=(account_sid, auth_token)
)

# Print the response
print(f"Status Code: {response.status_code}")
print()

# Parse and pretty-print the JSON response
try:
    response_json = response.json()
    print("Parsed Response:")
    print(json.dumps(response_json, indent=2))

    # Print key details
    if response.status_code == 201:
        print("\nMessage sent successfully!")
        print(f"  SID: {response_json.get('sid')}")
        print(f"  Status: {response_json.get('status')}")
        print(f"  To: {response_json.get('to')}")
        print(f"  From: {response_json.get('from')}")
    else:
        print(f"\nError: {response_json.get('message', 'Unknown error')}")
except Exception as e:
    print(f"Response is not JSON: {response.text}")
    print(f"Error: {e}")
