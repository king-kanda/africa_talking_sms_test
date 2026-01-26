# Infobip SMS Demo - Using Official SDK
import os
from dotenv import load_dotenv
from infobip_channels.sms.channel import SMSChannel

load_dotenv()

# Your Infobip credentials from https://portal.infobip.com/
base_url = os.getenv("INFOBIP_BASE_URL")  # e.g., "xxxxx.api.infobip.com"
api_key = os.getenv("INFOBIP_API_KEY")
sender = os.getenv("INFOBIP_SENDER", "InfoSMS")  # Sender ID or phone number

# Initialize the SMS channel
channel = SMSChannel.from_auth_params({
    "base_url": base_url,
    "api_key": api_key
})


def send_sms(to_number: str, message: str) -> dict:
    """
    Send an SMS message using Infobip.

    Args:
        to_number: Recipient phone number in E.164 format (e.g., +1234567890)
        message: The message content to send

    Returns:
        dict: Message details including message ID and status
    """
    sms_response = channel.send_sms_message({
        "messages": [
            {
                "destinations": [{"to": to_number}],
                "from": sender,
                "text": message
            }
        ]
    })

    # Extract response details
    if sms_response.messages:
        msg = sms_response.messages[0]
        return {
            "message_id": msg.message_id,
            "status": msg.status.name if msg.status else "unknown",
            "status_description": msg.status.description if msg.status else "",
            "to": msg.to,
        }
    return {"error": "No response received"}


def send_bulk_sms(recipients: list, message: str) -> list:
    """
    Send SMS to multiple recipients.

    Args:
        recipients: List of phone numbers in E.164 format
        message: The message content to send

    Returns:
        list: List of message details for each recipient
    """
    destinations = [{"to": number} for number in recipients]

    sms_response = channel.send_sms_message({
        "messages": [
            {
                "destinations": destinations,
                "from": sender,
                "text": message
            }
        ]
    })

    results = []
    if sms_response.messages:
        for msg in sms_response.messages:
            results.append({
                "message_id": msg.message_id,
                "status": msg.status.name if msg.status else "unknown",
                "to": msg.to,
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
