# 303-Weekender

#### Tee time notifications for high-handicappers only
_______________

This is a program designed to leverage the Twilio SMS API to send tee-time notifications for public golf courses in the Denver Metro Area. 
The program acts as a time trigger, sending an SMS notification to a specified user when tee-times go live for booking on your selected days of the week.
This was mostly designed so I can snag early morning times on Saturday and Sunday at different courses, and instead of scraping the site for times, it's so much easier just to send myself a reminder to look for the time when they are released online.
Currently, there are 16 public courses that you can recieve notifications for:
 
- Aurora Golf Courses
- Broken Tee
- CommonGround
- Denver Golf Courses
- DU Golf Club
- Foothills Recreation District
- Fossil Trace
- Green Valley Ranch
- Hyland Hills
- Indian Tree
- Lakewood Golf Courses
- Raccoon Creek
- Riverdale
- Saddleback
- Thorncreek
- West Woods

(Looking for new suggestions)

___________________________________
#### Twilio API
___________________________________
To make this app function, you will need to create an account on https://www.twilio.com/, buy a toll free number, and use the SID and authorization code provided within your code or environment variables. Currently, Twilio authorization in the program is loaded through environment variables in a .env file placed in the root directory:

```
from dotenv import load_dotenv

load_dotenv('twilio.env')
acct_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_tkn = os.getenv('TWILIO_AUTH_TOKEN')
from_phone = os.getenv('TWILIO_PHONE')
```

This snippet can be changed to reflect your account information instead of utilizing environment variables:
```
acct_sid = 'your acct sid'
auth_tkn = 'your account auth key'
from_phone = 'your twilio phone num')
```