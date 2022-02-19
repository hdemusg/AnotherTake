import os
from prettytable import from_csv
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Welcome to AnotherTake!",
    from_="+19034209599",
    to="+14702333985"
)

print(message.sid)