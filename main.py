import nsetools
import whatsapp
from datetime import datetime
from nsetools import Nse
import mail
import time
import yaml
import pandas as pd

if __name__ == "__main__":
    #Load the config file , See nse.yml
    with open(r'nse.yml') as file:
        data = yaml.full_load(file)

    for k , v in data["whatsapp"].items():
        if k == "contact_path" and v is not None:
            #contact_path : Holds fully qualified path of excel file . This file has a column 'Phone' that has 10 digit mobile numbers
            contact_path = v

    for k , v in data["email"].items(): 
        if k == "sender_email" and v is not None:
            sender_email = v
        if k == "sender_password" and v is not None:
            sender_password = v

    df = pd.read_excel(contact_path)
    df['Phone'] = df['Phone'].apply(lambda x: '+91' + str(x)) #Hardcoding +91 ext on India , Should be enhanced later
    nse = Nse()

    # Yes , while true is bad practice , For now kept 30 mins sleep ..hardcoding will be made configurable later
    while(True):
        print('Checking NIFTY 50 now : '+str(datetime.now()))
        d = nse.get_index_quote("nifty 50")
        for key , value in d.items():
            if key == "pChange":
                #Check if the percentage change is negative or positive , If negative send whatsapp
                if float(value) < 0:
                    whatsapp.sendWhatsApp(df['Phone'],value)
                   # print(df['Email'])
                 #   print(df['Email'].tolist())
                    mail.sendMailTo(sender_email,sender_password,df['Email'].dropna().tolist(),value)
                else:
                    print('Not sending notification as change is postive  : '+str(value))
        print('Going to sleep for 30 mins at '+ str(datetime.now()))
        time.sleep(60*30) # 30 mins sleep and check again