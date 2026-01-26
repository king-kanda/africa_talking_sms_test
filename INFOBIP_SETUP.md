# Infobip SMS Notification Demo - Setup Guide

This guide explains how to set up Infobip credentials and send SMS notifications using the Infobip API.

## Prerequisites

- Python 3.7 or higher
- An Infobip account (free trial available)
- pip (Python package manager)

## Step 1: Create an Infobip Account

1. Go to [Infobip Sign Up](https://www.infobip.com/signup)
2. Create a free account
3. Verify your email address
4. Complete your profile setup

## Step 2: Get Your Infobip Credentials

After signing up, find your credentials in the [Infobip Portal](https://portal.infobip.com/):

### API Key
1. Go to the Infobip Portal
2. Click on your profile icon (top right)
3. Select **"API Keys"** or navigate to **Settings > API Keys**
4. Create a new API key or copy an existing one

### Base URL
1. Your unique Base URL is shown on the portal homepage
2. It looks like: `xxxxxx.api.infobip.com`
3. You can also find it under **Settings > API Keys**

### Sender ID
- For trial accounts, use `InfoSMS` or the default sender
- For production, you can register custom Sender IDs (alphanumeric or phone numbers)

## Step 3: Configure Environment Variables

Create a `.env` file in the project root with your credentials:

```bash
# Infobip Credentials
INFOBIP_BASE_URL=xxxxxx.api.infobip.com
INFOBIP_API_KEY=your_api_key_here
INFOBIP_SENDER=InfoSMS
```

**Important Security Notes:**
- Never commit your `.env` file to version control
- The `.gitignore` file already excludes `.env`
- Keep your API Key secret - it provides access to your account

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Infobip SDK directly:

```bash
pip install infobip-api-python-sdk python-dotenv
```

## Step 5: Run the Demo

### Using the Official SDK (Recommended)

```bash
python infobip_sms.py
```

### Using Direct HTTP Requests

```bash
python infobip_sms_direct.py
```

## Trial Account Information

With an Infobip trial account:

1. **Free Credits**: New accounts receive free trial credits
2. **Limited Destinations**: Some destination countries may be restricted
3. **Sender ID**: Use `InfoSMS` or default sender during trial
4. **Rate Limits**: Trial accounts have lower rate limits

## Phone Number Format

Infobip requires phone numbers in E.164 format (international format without spaces or dashes):

| Country | Format | Example |
|---------|--------|---------|
| USA | +1XXXXXXXXXX | +14155551234 |
| UK | +44XXXXXXXXXX | +447911123456 |
| Kenya | +254XXXXXXXXX | +254712345678 |
| Nigeria | +234XXXXXXXXXX | +2348012345678 |
| Germany | +49XXXXXXXXXXX | +4915123456789 |

## Sender ID Options

### Alphanumeric Sender ID
- Up to 11 characters (letters and numbers)
- Example: `MyCompany`, `InfoSMS`
- Not supported in all countries (e.g., USA requires phone numbers)

### Numeric Sender ID (Phone Number)
- Use your registered phone number
- Required for two-way SMS
- Example: `+14155551234`

### Shortcode
- Short numeric codes (4-6 digits)
- Requires separate registration
- Example: `12345`

## API Features

Infobip offers advanced SMS features:

### Delivery Reports
```python
# Request delivery reports
payload = {
    "messages": [{
        "destinations": [{"to": "+1234567890"}],
        "from": "InfoSMS",
        "text": "Hello!",
        "notifyUrl": "https://your-webhook.com/delivery"
    }]
}
```

### Scheduled Messages
```python
# Send at a specific time
payload = {
    "messages": [{
        "destinations": [{"to": "+1234567890"}],
        "from": "InfoSMS",
        "text": "Scheduled message",
        "sendAt": "2024-12-31T23:59:59.000+00:00"
    }]
}
```

### Flash SMS
```python
# Send flash/popup SMS
payload = {
    "messages": [{
        "destinations": [{"to": "+1234567890"}],
        "from": "InfoSMS",
        "text": "Flash message!",
        "flash": True
    }]
}
```

## Troubleshooting

### Error: "UNAUTHORIZED" (401)
- **Cause**: Invalid API Key
- **Fix**: Verify your API key in the `.env` file

### Error: "BAD_REQUEST" (400)
- **Cause**: Invalid request format or missing required fields
- **Fix**: Check your payload structure and phone number format

### Error: "INVALID_DESTINATION_ADDRESS"
- **Cause**: Phone number format is incorrect
- **Fix**: Use E.164 format (e.g., +1234567890)

### Error: "REJECTED_DESTINATION"
- **Cause**: Destination country not allowed for trial account
- **Fix**: Upgrade account or test with allowed countries

### Error: "MISSING_API_KEY"
- **Cause**: API Key not provided in headers
- **Fix**: Ensure `Authorization: App {api_key}` header is set

## API Documentation

- [Infobip SMS API Docs](https://www.infobip.com/docs/sms)
- [Infobip Python SDK](https://github.com/infobip/infobip-api-python-sdk)
- [Infobip Portal](https://portal.infobip.com/)
- [API Reference](https://www.infobip.com/docs/api)
- [Pricing Calculator](https://www.infobip.com/pricing)

## Code Examples

### Send a Single SMS

```python
from infobip_channels.sms.channel import SMSChannel

channel = SMSChannel.from_auth_params({
    "base_url": "xxxxx.api.infobip.com",
    "api_key": "your_api_key"
})

response = channel.send_sms_message({
    "messages": [{
        "destinations": [{"to": "+1234567890"}],
        "from": "InfoSMS",
        "text": "Hello from Infobip!"
    }]
})
print(response)
```

### Send to Multiple Recipients

```python
recipients = ["+1111111111", "+2222222222", "+3333333333"]
destinations = [{"to": number} for number in recipients]

response = channel.send_sms_message({
    "messages": [{
        "destinations": destinations,
        "from": "InfoSMS",
        "text": "Bulk notification message"
    }]
})

for msg in response.messages:
    print(f"Sent to {msg.to}: {msg.message_id} - {msg.status.name}")
```

### Get Delivery Reports

```python
# Fetch delivery reports for sent messages
reports = channel.get_outbound_sms_delivery_reports()
for report in reports.results:
    print(f"Message {report.message_id}: {report.status.name}")
```

## Comparison with Other Providers

| Feature | Infobip | Twilio | Africa's Talking |
|---------|---------|--------|------------------|
| Global Coverage | 190+ countries | 180+ countries | Africa-focused |
| Free Trial | Yes | Yes | Yes (Sandbox) |
| 2-Way SMS | Yes | Yes | Yes |
| Delivery Reports | Yes | Yes | Yes |
| WhatsApp | Yes | Yes | No |
| Viber | Yes | No | No |
