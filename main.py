import nsetools
import whatsapp
from nsetools import Nse
import mail
nse = Nse()
d = nse.get_index_quote("nifty 50")
sender_whatsapp_list = ["+91-9999999999"] # some dummy number
sender_list =["test@gmail.com","test@gmail.com"] #some dummy email 
for key , value in d.items():
    if key == "pChange":
        if(float(value) > 2):
            mail.sendMailTo(sender_list,value)
            whatsapp.sendWhatsApp(sender_whatsapp_list,value)
