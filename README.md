# 303-Weekender Beta

#### Tee time notifications for high-handicappers only
#### Text 'Begin' to (855) 643-7385 to start receiving notifications for tee times in the Denver Metro Area
_______________

This is a program designed to leverage the Twilio SMS API to send tee-time notifications for public golf courses in the Denver Metro Area. 
The program acts as a time trigger, sending an SMS notification to a specified user when tee-times go live for booking on your selected days of the week.
This was mostly designed so I can snag early morning times on Saturday and Sunday at different courses, and instead of scraping the sites for times, it's so much easier just to send myself a reminder to look for times when they are released online.
Currently, there are 16 public courses that you can receive notifications for:
 
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

__________________________________
#### Notification Engine (main.py)
___________________________________

The notification engine is run through main.py, which assesses the current time and sends SMS notifications at the target time based on the user's chosen courses and days of the week. To
accomplish this, I leveraged the Twilio SMS API and arrow to create time-zone aware datetimes for use in the program. The notification engine runs through a series of functions designed to send the user a notification if one of the time triggers matches the current time within the program.

__________________________________
#### Response Engine (flask_app.py)
__________________________________

The response engine is run through flask_app.py, which is desgined to take user inputs through SMS texts and apply those inputs to a sqlite3 database within user_db.py. The Flask app acts as a webhook, connected to the Twilio SMS API through ngrok port forwarding on my local machine.
After information is collected from the user and the subscription is active, the main.py script loops through the collected user data once per second in order to trigger a notification when tee times are released online.

_________________________________
#### Who cares how it works?
_________________________________

As long as it runs, amirite? Take it for a test drive by texting 'Begin' to (855) 643-7385, enter up to 4 days of the week that you would like a tee time for, then select up to 10 courses. You will receive an SMS notification when tee times go live at those specific courses for your chosen days.