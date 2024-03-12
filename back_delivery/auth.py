import random 
import string
from twilio.rest import Client  

# Generate a one time password
def generate_otp(length=6):
    chars = string.digits
    otp = ''.join(random.choice(chars) for _ in range(length))
    return otp

# Send one time password via phone

def send_otp_phone(phone_number, otp):
    account_sid = 'ACabda1e60dda22b650ad88f5f6bacb635'  # Replace with your Twilio account SID
    auth_token = '66f65e7ae7c0b88febfb223ffd2c410d'  # Replace with your Twilio auth token
    twilio_phone_number = '+16124008603'  # Replace with your Twilio phone number


    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = f'Your one time password: {otp}',
        from_ = twilio_phone_number,
        to = phone_number
)