from twilio.rest import TwilioRestClient
from flask import Flask, request
import twilio.twiml
import os

# Pull in configuration from system environment variables
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

app = Flask(__name__)

callers = {
	"+19251111111": "Katie",
	"+19252222222": "Walter",
	"+19253333333": "Megan"
}

@app.route("/", methods=["GET", "POST"])
def hello_custom():
	from_number = request.values.get('From')
	if from_number in callers:
		name = callers[from_number]
	else:
		name = "Hacker"
	message = "Hello, {}, thanks for the message!".format(name)
	resp = twilio.twiml.Response()
	resp.message(message)
	return str(resp)


if __name__ == "__main__":
	app.run(debug=True)