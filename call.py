import os
from dotenv import load_dotenv
from twilio.rest import Client

#load environment variables 
load_dotenv()

def make_call(to_number):
    try:
        #Initialize twilio client
        client = Client(
            os.getenv('TWILIO_ACCOUNT_SID'),
            os.getenv('TWILIO_AUTH_TOKEN')
        )

        #Make the call
        call = client.calls.create(
            url="http://demo.twilio.com/docs/voice.xml",
            to=to_number,
            from_= os.getenv('TWILIO_PHONE_NUMBER')
        )

        print(f"📞 Calling {to_number}...")
        print(f"Call SID: {call.sid}")
        return True
    
    except Exception as e:
        print(f"Error making call: {e}")
        return False
    
if __name__ == "__main__":
    #Get recipient number from user
    recipient = input("Enter phone number to call: ")

    #Make the call
    make_call(recipient)