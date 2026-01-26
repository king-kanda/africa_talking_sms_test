# Infobip SMS Demo - Direct HTTP Request (without SDK)
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Your Infobip credentials
base_url = os.getenv("INFOBIP_BASE_URL")  # e.g., "xxxxx.api.infobip.com"
api_key = os.getenv("INFOBIP_API_KEY")
sender = os.getenv("INFOBIP_SENDER", "InfoSMS")

# Infobip SMS API endpoint
url = f"https://{base_url}/sms/2/text/advanced"

# Request headers
headers = {
    "Authorization": f"App {api_key}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Debug info (without exposing full credentials)
print(f"Base URL: {base_url}")
print(f"API Key: {api_key[:8]}...{api_key[-4:] if api_key else 'N/A'}")
print(f"Sender: {sender}")
print()

# Request payload (JSON format)
payload = {
    "messages": [
        {
            "destinations": [
                {"to": "+1234567890"}  # Replace with recipient number in E.164 format
            ],
            "from": sender,
            "text": "Hello! This is a test message from Infobip API (direct HTTP request)."
        }
    ]
}

# Make the request
print("Sending SMS request...")
print(f"Endpoint: {url}")
print(f"Payload: {json.dumps(payload, indent=2)}")
print()

# Send request
response = requests.post(
    url,
    headers=headers,
    json=payload
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
    if response.status_code == 200:
        messages = response_json.get("messages", [])
        if messages:
            print("\nMessage Details:")
            for msg in messages:
                print(f"  Message ID: {msg.get('messageId')}")
                print(f"  To: {msg.get('to')}")
                status = msg.get("status", {})
                print(f"  Status: {status.get('name')} - {status.get('description')}")
    else:
        error = response_json.get("requestError", {}).get("serviceException", {})
        print(f"\nError: {error.get('text', 'Unknown error')}")
        print(f"Message ID: {error.get('messageId', 'N/A')}")
except Exception as e:
    print(f"Response is not JSON: {response.text}")
    print(f"Error: {e}")
