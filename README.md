# Africa's Talking API Testing

Test project for Africa's Talking SMS API using Python.

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API credentials:**
   - Copy `.env.example` to `.env`
   - Get your API credentials from [Africa's Talking Dashboard](https://account.africastalking.com/)
   - Update `.env` with your credentials:
     ```
     AT_USERNAME=sandbox  # or your production username
     AT_API_KEY=your_actual_api_key
     AT_SENDER_ID=your_shortcode_or_alphanumeric
     ```

3. **For Sandbox Testing:**
   - Username: `sandbox`
   - Get sandbox API key from: https://account.africastalking.com/apps/sandbox
   - Use test phone numbers from the sandbox

## Running Tests

1. **Edit test_sms.py:**
   - Update `test_recipients` with your phone number(s) in international format
   - Uncomment the `send_sms()` line to actually send SMS

2. **Run the test script:**
   ```bash
   python test_sms.py
   ```

## Phone Number Format

Phone numbers must be in international format:
- Kenya: `+254712345678`
- Nigeria: `+2348012345678`
- Uganda: `+256712345678`
- etc.

## API Documentation

- [Africa's Talking SMS API Docs](https://developers.africastalking.com/docs/sms/overview)
- [Python SDK Documentation](https://github.com/AfricasTalkingLtd/africastalking-python)
