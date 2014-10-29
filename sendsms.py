from twilio.rest import TwilioRestClient
import os

# Pull in configuration from system environment variables
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
number_to_text = "+19253304141"

message = client.messages.create(from_=TWILIO_NUMBER,
								to=number_to_text,
								body="Hello from Hackbright Twilio Workshop")
print message.sid