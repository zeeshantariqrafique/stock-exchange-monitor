# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
import yaml

def send_mail_to(sender_email: str,
                 sender_password: str,
                 reciever_list: str,
                 nifty_change: str) -> None:
    try:
        for e in reciever_list:
            print(e)
            # creates SMTP session 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
  
            # start TLS for security 
            s.starttls() 
  
            # Authentication 
            s.login(sender_email, sender_password) 
  
            # message to be sent 
            message = "Nifty 50 Index has changed by " + str(nifty_change) 
  
            # sending the mail 
            s.sendmail(sender_email , e, message) 
            print('Sent email to :'+e)
            # terminating the session 
            s.quit()
        return True            
    except Exception:
        print("error while sending mail")
        s.quit()
        return False


#Load the config file , See nse.yml
with open(r'nse.yml') as file:
    data = yaml.full_load(file)

if __name__ == "__main__":
    test_email_list = ["rafiquezeeshan90@gmail.com"]
    for k , v in data["email"].items(): 
        if k == "sender_email" and v is not None:
            sender_email = v
            print(sender_email)
        if k == "sender_password" and v is not None:
            sender_password = v
    assert send_mail_to(sender_email,sender_password,test_email_list,10)