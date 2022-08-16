import os
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime, timedelta

def check_intersection(user,desired,courses):
    set_available = set([d['id'] for d in courses])  
    set_desired = set(desired[user])
    open = set_available.intersection(set_desired)
    return open

def make_call(users, courses):
    utc_dt = datetime.utcnow()
    ist_dt = utc_dt + timedelta(hours=5.5)
    current_time = ist_dt.strftime("%H:%M:%S")
    
    load_dotenv()
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    #desired specific list
    desired_1 = ['76770','96730','96727','86208','78302','98225','86207','98388','78322']
    desired_2 = ['97807','77802','83405'] 
    desired_3 = ['96730','78322'] 

    desired_4 = ['78302', '98225','96292']          


    desired = [desired_1,desired_2, desired_3, desired_4]

    for i,user in enumerate(users):
        num = os.getenv(user)
        #print(num)
        open = check_intersection(i,desired,courses)
        #ab all day calling

        if(len(open) > 0):
            if user == 'NUM_3' or user == 'NUM_2' or user == 'NUM_1':
                call = client.calls.create(
                    twiml='<Response><Say>Hello ' + user + ', your desired courses are open!</Say></Response>',
                    to = num,
                    from_ = '+19403737261'  
                )
                print(call.sid)
        #others only day time
        # if(current_time >= '07:00:00' and current_time <= '23:00:00'):
        #     if(len(open) > 0):
        #         call = client.calls.create(
        #             twiml='<Response><Say>Hello ' + user + ', your desired courses are open!</Say></Response>',
        #             to = num,
        #             from_ = '+19403737261'  
        #         )
        #         print(call.sid)
        # else:
        #     print("not calling becase night")