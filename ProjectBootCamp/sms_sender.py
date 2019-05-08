
from twilio.rest import Client

"importing Client class from twilio API"

"Creating a Sms sender class to send SMS"


class SmsSender:
    "those things which would remain constant, placing them in initializing function"

    def __init__(self, sid, auth_token, from_number):

         #Creating an object of Client class

        self.client = Client(sid, auth_token)
         #from number
        self.from_number = from_number

    "defining a send function for SmsSend class which will send message to different people"

    def send(self, to_number, msg_text):
        message = self.client.messages \
        .create(
        to=to_number,
        from_=self.from_number,
        body=msg_text
        )

        "printing sid of message to check whether the message was sent or not"
        print('message sent successfully ' + message.sid)

#======================================================================

"initializing and creating SmsSender Class object by giving it sid, auth_token and from number"



SmsSender=SmsSender(sid='ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                    auth_token='your_auth_token', #enter the auth_token you would get from twilio's website.
                    from_number='+12014845940'
                    )

"Creating a sms sender programm for a general user"

while(True):
    
    print("\n Bulk SMS sender\n")
    print("Please enter the message text & the message recipient's number in a +xxxxxxx format\n") # displaying instructions
    
    msg_txt= input("Please enter the message text:\n")
    num_1 = input("Please enter the recipient number:\n")  # taking input from user
    # error checking for invalid number entry
    try:
        recipent_number=num_1
        num_1 = int (num_1)
    except:
        print("Invalid number entered")
        continue

    recipent_number='+'+ recipent_number[1:]
    
    SmsSender.send(to_number=recipent_number, msg_text=msg_txt) # passing argument to send method of SmsSender class

    # Asking user whether he wants to continue using calculator
    con = input("if you wish to continue press Y, or press N to end program:\n")
    if con == 'Y':
        continue  # returns to top of loop starts calculating again
    else:
        break  # Ending the program

print("\n end of program")



