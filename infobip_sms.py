# Infobip SMS Demo - Using HTTP Requests
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Your Infobip credentials from https://portal.infobip.com/
base_url = os.getenv("INFOBIP_BASE_URL")  # e.g., "xxxxx.api.infobip.com"
api_key = os.getenv("INFOBIP_API_KEY")
sender = os.getenv("INFOBIP_SENDER", "InfoSMS")  # Sender ID or phone number


def send_sms(to_number: str, message: str) -> dict:
    """
    Send an SMS message using Infobip.

    Args:
        to_number: Recipient phone number in E.164 format (e.g., +1234567890)
        message: The message content to send

    Returns:
        dict: Message details including message ID and status
    """
    url = f"https://{base_url}/sms/2/text/advanced"

    headers = {
        "Authorization": f"App {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "messages": [
            {
                "destinations": [{"to": to_number}],
                "from": sender,
                "text": message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()

    if response.status_code == 200 and response_json.get("messages"):
        msg = response_json["messages"][0]
        status = msg.get("status", {})
        return {
            "message_id": msg.get("messageId"),
            "status": status.get("name", "unknown"),
            "status_description": status.get("description", ""),
            "to": msg.get("to"),
        }

    # Handle error response
    error = response_json.get("requestError", {}).get("serviceException", {})
    return {
        "error": error.get("text", "Unknown error"),
        "status_code": response.status_code
    }


def send_bulk_sms(recipients: list, message: str) -> list:
    """
    Send SMS to multiple recipients.

    Args:
        recipients: List of phone numbers in E.164 format
        message: The message content to send

    Returns:
        list: List of message details for each recipient
    """
    url = f"https://{base_url}/sms/2/text/advanced"

    headers = {
        "Authorization": f"App {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    destinations = [{"to": number} for number in recipients]

    payload = {
        "messages": [
            {
                "destinations": destinations,
                "from": sender,
                "text": message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()

    results = []
    if response.status_code == 200 and response_json.get("messages"):
        for msg in response_json["messages"]:
            status = msg.get("status", {})
            results.append({
                "message_id": msg.get("messageId"),
                "status": status.get("name", "unknown"),
                "to": msg.get("to"),
            })
    return results


if __name__ == "__main__":
    # Example: Send a test SMS
    # Update this number to your test recipient
    test_recipient = "+1234567890"  # Replace with actual number in E.164 format
    test_message = "Hello! This is a test message from Infobip."

    print(f"Sending SMS to {test_recipient}...")
    response = send_sms(test_recipient, test_message)
    print("Response:")
    for key, value in response.items():
        print(f"  {key}: {value}")
