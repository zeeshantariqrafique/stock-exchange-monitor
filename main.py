import nsetools
from nsetools import Nse
import mail
nse = Nse()
d = nse.get_index_quote("nifty 50")
sender_list =["test@gmail.com","test@gmail.com"]
for key in d:
    if key == "pChange":
        if(float(d[key]) > 2):
            mail.sendMailTo(sender_list,d[key])
