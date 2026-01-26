# Twilio SMS Notification Demo - Setup Guide

This guide explains how to set up Twilio credentials and send SMS notifications using the Twilio API.

## Prerequisites

- Python 3.7 or higher
- A Twilio account (free trial available)
- pip (Python package manager)

## Step 1: Create a Twilio Account

1. Go to [Twilio Sign Up](https://www.twilio.com/try-twilio)
2. Create a free account (no credit card required for trial)
3. Verify your email address
4. Verify your phone number (this will be your first verified number)

## Step 2: Get Your Twilio Credentials

After signing up, you'll find your credentials on the [Twilio Console Dashboard](https://console.twilio.com/):

1. **Account SID**: Found on the main dashboard (starts with `AC`)
2. **Auth Token**: Found on the main dashboard (click "Show" to reveal)
3. **Twilio Phone Number**: Get a free phone number from the console
   - Go to: [Phone Numbers > Manage > Buy a number](https://console.twilio.com/us1/develop/phone-numbers/manage/search)
   - Or use the trial number provided

## Step 3: Configure Environment Variables

Create a `.env` file in the project root with your credentials:

```bash
# Twilio Credentials
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
```

**Important Security Notes:**
- Never commit your `.env` file to version control
- The `.gitignore` file should already exclude `.env`
- Keep your Auth Token secret - it provides full access to your account

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Twilio directly:

```bash
pip install twilio python-dotenv
```

## Step 5: Run the Demo

### Using the Official SDK (Recommended)

```bash
python twilio_sms.py
```

### Using Direct HTTP Requests

```bash
python twilio_sms_direct.py
```

## Trial Account Limitations

With a Twilio trial account:

1. **Verified Numbers Only**: You can only send SMS to phone numbers you've verified
   - Verify numbers at: [Verified Caller IDs](https://console.twilio.com/us1/develop/phone-numbers/manage/verified)

2. **Trial Message Prefix**: All messages include "Sent from your Twilio trial account" prefix

3. **Limited Credits**: Trial accounts come with free credits (~$15.50 USD)

4. **Geographic Restrictions**: Some countries may not be available during trial

## Phone Number Format

Twilio requires phone numbers in E.164 format:

| Country | Format | Example |
|---------|--------|---------|
| USA | +1XXXXXXXXXX | +14155551234 |
| UK | +44XXXXXXXXXX | +447911123456 |
| Kenya | +254XXXXXXXXX | +254712345678 |
| Nigeria | +234XXXXXXXXXX | +2348012345678 |

## Upgrading to Production

To remove trial limitations:

1. Go to [Billing > Upgrade](https://console.twilio.com/us1/billing/manage-billing/upgrade)
2. Add a payment method
3. Fund your account
4. Your messages will no longer have the trial prefix

## Troubleshooting

### Error: "Unable to create record: The 'To' number is not a verified number"
- **Cause**: Trial accounts can only send to verified numbers
- **Fix**: Verify the recipient number in your Twilio console

### Error: "Account not authorized to call"
- **Cause**: Geographic permissions not enabled
- **Fix**: Enable permissions at: Console > Messaging > Settings > Geo permissions

### Error: "Authentication Error"
- **Cause**: Invalid Account SID or Auth Token
- **Fix**: Double-check credentials in your `.env` file

### Error: "The 'From' phone number is not a valid"
- **Cause**: Invalid or unowned Twilio phone number
- **Fix**: Ensure `TWILIO_PHONE_NUMBER` is a number you own in Twilio

## API Documentation

- [Twilio SMS API Docs](https://www.twilio.com/docs/sms)
- [Twilio Python SDK](https://www.twilio.com/docs/libraries/python)
- [Twilio Console](https://console.twilio.com/)
- [Twilio Pricing](https://www.twilio.com/sms/pricing)

## Code Examples

### Send a Single SMS

```python
from twilio.rest import Client

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Hello from Twilio!",
    from_="+1234567890",
    to="+0987654321"
)
print(message.sid)
```

### Send to Multiple Recipients

```python
recipients = ["+1111111111", "+2222222222", "+3333333333"]
for number in recipients:
    message = client.messages.create(
        body="Bulk notification message",
        from_=twilio_phone_number,
        to=number
    )
    print(f"Sent to {number}: {message.sid}")
```

### Check Message Status

```python
message = client.messages(message_sid).fetch()
print(f"Status: {message.status}")  # queued, sending, sent, delivered, failed
```
