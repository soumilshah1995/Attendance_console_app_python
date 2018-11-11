# we import the Twilio client from the dependency we just installed
from twilio.rest import Client


def send_sms():




    # the following line needs your Twilio Account SID and Auth Token
    client = Client("XXXXX", "XXXXXX")
    client.messages.create(to="+XXXX",
                           from_="+XXXX",
                           body="Hello from Python!")

    return True

