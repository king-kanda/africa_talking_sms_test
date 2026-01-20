import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


# Your credentials
username = os.getenv("AT_USERNAME")
api_key = os.getenv("AT_API_KEY")

# Sandbox endpoint (correct endpoint is /messaging not /messaging/bulk)
url = "https://api.sandbox.africastalking.com/version1/messaging"

# Request headers - try different variations
headers = {
    "Accept": "application/json",
    "apiKey": api_key,
    "Content-Type": "application/x-www-form-urlencoded"
}

# Also print headers for debugging (without exposing full API key)
print(f"Headers: Accept, apiKey (ending with ...{api_key[-8:]}), Content-Type")

# Request payload (form-encoded data)
payload = {
    "username": username,
    "to": "+254759626677",  # single recipient
    "message": "Hello! This is a test message from AfricasTalking API."
}

# Make the request
print("Sending SMS request...")
print(f"Endpoint: {url}")
print(f"Payload: {payload}")
print()

# Send as form data (not JSON)
response = requests.post(url, headers=headers, data=payload)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
print()

# Parse and pretty-print if JSON
try:
    response_json = response.json()
    print("Parsed Response:")
    print(json.dumps(response_json, indent=2))
except:
    print("Response is not JSON")
