# Twilio SMS Demo - Using Official SDK
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Your Twilio credentials from https://console.twilio.com/
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")  # Your Twilio phone number

# Initialize the Twilio client
client = Client(account_sid, auth_token)


def send_sms(to_number: str, message: str) -> dict:
    """
    Send an SMS message using Twilio.

    Args:
        to_number: Recipient phone number in E.164 format (e.g., +1234567890)
        message: The message content to send

    Returns:
        dict: Message details including SID, status, and date
    """
    message_response = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to_number
    )

    return {
        "sid": message_response.sid,
        "status": message_response.status,
        "to": message_response.to,
        "from": message_response.from_,
        "date_created": str(message_response.date_created),
    }


if __name__ == "__main__":
    # Example: Send a test SMS
    # Update this number to your test recipient
    test_recipient = "+1234567890"  # Replace with actual number in E.164 format
    test_message = "Hello! This is a test message from Twilio."

    print(f"Sending SMS to {test_recipient}...")
    response = send_sms(test_recipient, test_message)
    print("Response:")
    for key, value in response.items():
        print(f"  {key}: {value}")
