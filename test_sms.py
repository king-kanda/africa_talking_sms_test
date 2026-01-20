# import package
import africastalking

username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "atsk_71061f1213fd80094295c0bb4cef6613d151801a1bbbefdc1894484ad8dac4cf2825c1c6"

africastalking.initialize(username.strip(), api_key.strip())
sms = africastalking.SMS

if __name__ == "__main__":
    # Use the service synchronously
    response = sms.send("Hello Message! bitaa", ["+254759626677"])
    print(response)