
from twilio.rest import Client

TWILIO_SID = _______
TWILIO_AUTH_TOKEN = _______
TWILIO_VIRTUAL_NUMBER = _______
TWILIO_VERIFIED_NUMBER = _______


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)