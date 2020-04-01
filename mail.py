# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
import yaml

def sendMailTo(senderEmail,senderPassword,receiverList,niftyChange):
    try:
        for e in receiverList:
            print(e)
            # creates SMTP session 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
  
            # start TLS for security 
            s.starttls() 
  
            # Authentication 
            s.login(senderEmail, senderPassword) 
  
            # message to be sent 
            message = "Nifty 50 Index has changed by " + str(niftyChange) 
  
            # sending the mail 
            s.sendmail(senderEmail , e, message) 
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
    testMailList = ["rafiquezeeshan90@gmail.com"]
    for k , v in data["email"].items(): 
        if k == "sender_email" and v is not None:
            sender_email = v
            print(sender_email)
        if k == "sender_password" and v is not None:
            sender_password = v
    assert sendMailTo(sender_email,sender_password,testMailList,10)