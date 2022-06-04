import whatsapp
from datetime import datetime
from nsetools import Nse
import mail
import time
import yaml
import pandas as pd

def main():
    #Load the config file , See nse.yml
    with open(r'nse.yml') as file:
        data = yaml.full_load(file)
    
    config = {**data["app"]}

    df = pd.read_excel(config['contact_path'])

    df['Phone'] = df['Phone'].apply(lambda x: '+91' + str(x)) #Hardcoding +91 ext on India , Should be enhanced later
    nse = Nse()

    # Yes , while true is bad practice , For now kept 30 mins sleep ..hardcoding will be made configurable later
    while(True):
        print(f'Checking NIFTY 50 now : {str(datetime.now())}')
        d = nse.get_index_quote("nifty 50")
        for key , value in d.items():
            if key == "pChange":
                #Check if the percentage change is negative or positive , If negative send whatsapp
                if float(value) < 0:
                    whatsapp.sendWhatsApp(df['Phone'],value)
                    mail.sendMailTo(config['sender_email'],config['sender_password'],df['Email'].dropna().tolist(),value)
                else:
                    print('Not sending notification as change is postive  : '+str(value))
        sleep = config['sleep_in_minutes']
        print(f'Going to sleep for {sleep} mins at {str(datetime.now())}')
        time.sleep(int(sleep)) 


if __name__ == "__main__":
    main()