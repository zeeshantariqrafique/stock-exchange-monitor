import os
from datetime import datetime
from twilio.rest import Client


from_whatsapp_number='whatsapp:+14155238886'

def sendWhatsApp(list_numbers,nifty_change):
    msg = '''Hi, 
        This message is to inform you that Nifty 50 Index has changed by ''' + str(nifty_change) + '%' + ' as of ' + str(datetime.now())
    for number in list_numbers:  
        to_num ='whatsapp:' + number
        client= Client()
        client.messages.create(body=msg,from_=from_whatsapp_number,to=to_num)
        print('Sending whatsapp to '+ number)