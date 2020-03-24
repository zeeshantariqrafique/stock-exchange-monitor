# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 


def sendMailTo(receiverList,niftyChange):
    for e in receiverList:
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        # start TLS for security 
        s.starttls() 
  
        # Authentication 
        s.login("test@gmail.com", "test") 
  
        # message to be sent 
        message = "Nifty 50 INdex has changed by " + str(niftyChange) 
  
        # sending the mail 
        s.sendmail("test@gmail.com", e, message) 
  
        # terminating the session 
        s.quit()