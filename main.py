from twilio.rest import Client
import os
import time
import datetime
import arrow
from dotenv import load_dotenv
import flask_app

flask_app.app()

load_dotenv('twilio.env')
acct_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_tkn = os.getenv('TWILIO_AUTH_TOKEN')
from_phone = os.getenv('TWILIO_PHONE')


class TeeSheet:
    def __init__(self, tee_sheet_name, specifications, tee_timedelta, website, phone):
        self.tee_sheet_name = str(tee_sheet_name)
        self.courses_served = []
        self.specifications = str(specifications)
        self.tee_timedelta = tee_timedelta
        self.website = str(website)
        self.phone = str(phone)

    def add_course_served(self, course_name):
        self.courses_served.append(course_name)

    def get_send_times(self, num_dys, tgt1, tgt2, tgt3, tgt4, tgt5, tgt6, tgt7, tgt8, tgt9, tgt10, tgt11, tgt12, tgt13, tgt14, tgt15, tgt16, tgt17, tgt18, tgt19, tgt20):
        target_1_comp = ""
        target_2_comp = ""
        target_3_comp = ""
        target_4_comp = ""
        target_5_comp = ""
        target_6_comp = ""
        target_7_comp = ""
        target_8_comp = ""
        target_9_comp = ""
        target_10_comp = ""
        target_11_comp = ""
        target_12_comp = ""
        target_13_comp = ""
        target_14_comp = ""
        target_15_comp = ""
        target_16_comp = ""
        target_17_comp = ""
        target_18_comp = ""
        target_19_comp = ""
        target_20_comp = ""

        if num_dys >= 1:
            target_1_comp = (tgt1 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_2_comp = (tgt2 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_3_comp = (tgt3 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_4_comp = (tgt4 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_5_comp = (tgt5 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
        if num_dys >= 2:
            target_6_comp = (tgt6 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_7_comp = (tgt7 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_8_comp = (tgt8 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_9_comp = (tgt9 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_10_comp = (tgt10 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
        if num_dys >= 3:
            target_11_comp = (tgt11 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_12_comp = (tgt12 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_13_comp = (tgt13 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_14_comp = (tgt14 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_15_comp = (tgt15 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
        if num_dys == 4:
            target_16_comp = (tgt16 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_17_comp = (tgt17 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_18_comp = (tgt18 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_19_comp = (tgt19 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")
            target_20_comp = (tgt20 - self.tee_timedelta).strftime("%Y-%m-%d %H:%M:%S")

        return target_1_comp, target_2_comp, target_3_comp, target_4_comp, target_5_comp, target_6_comp, \
               target_7_comp, target_8_comp, target_9_comp, target_10_comp, target_11_comp, target_12_comp, \
               target_13_comp, target_14_comp, target_15_comp, target_16_comp, target_17_comp, target_18_comp, \
               target_19_comp, target_20_comp

    def send_trigger(self, phn_num, num_dys, curr_local_str, tgt1_cs, tgt2_cs, tgt3_cs, tgt4_cs, tgt5_cs, tgt6_cs, tgt7_cs, tgt8_cs, tgt9_cs, tgt10_cs, tgt11_cs, tgt12_cs, tgt13_cs, tgt14_cs, tgt15_cs, tgt16_cs, tgt17_cs, tgt18_cs, tgt19_cs, tgt20_cs,
                     tgt1, tgt2, tgt3, tgt4, tgt5, tgt6, tgt7, tgt8, tgt9, tgt10, tgt11, tgt12, tgt13, tgt14, tgt15, tgt16, tgt17, tgt18, tgt19, tgt20):
        if num_dys >= 1:
            if tgt1_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt1, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt2_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt2, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt3_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt3, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt4_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt4, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt5_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt5, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
        if num_dys >= 2:
            if tgt6_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt6, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt7_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt7, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt8_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt8, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt9_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt9, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt10_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt10, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
        if num_dys >= 3:
            if tgt11_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt11, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt12_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt12, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt13_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt13, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt14_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt14, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt15_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt15, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
        if num_dys == 4:
            if tgt16_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt16, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt17_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt17, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt18_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt18, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt19_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt19, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')
            if tgt20_cs == curr_local_str:
                msg = create_notification(user, self.tee_sheet_name, tgt20, self.website, self.phone)
                send_message(msg, phn_num)
                print(f'Notification for {self.tee_sheet_name} sent to {phn_num} ({curr_local_str})')


# Function to create the message when it is time to send the message
def create_notification(usr, tee_sheet_name, target_date, website, phone):
    notification = f'Hi {usr}, {tee_sheet_name} tee times for {target_date.strftime("%A, %B %#d")} are now available on the website\n' \
                   f'\n' \
                   f'Book now: {website}\n' \
                   f'\n' \
                   f'Call the golf shop: {phone}'
    return notification


# Function to create the setup notification at the start of the program
def create_setup_notification(usr, dy_list, crse_list):
    notification = f"Hi {usr},\n" \
                   f"\n" \
                   f"You have been subscribed for tee time notifications on {dy_list} for the following courses: {crse_list}\n" \
                   f"\n" \
                   f"Welcome to the alpha test for 303-Weekender. Text Ryan Peet to STOP or configure your settings."
    return notification


# Function to send the message when it is time to send the message
def send_message(message_text, num_to):
    account_sid = acct_sid
    auth_token = auth_tkn
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_text,
        from_=from_phone,
        to=num_to)
    print(f'\n{message.sid}')


# Function to find the next target dates at any given moment
def target_dates(curr_date, indexes):
    target_date_list = []
    for b in indexes:
        days_ahead = b - curr_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        target_date1 = curr_date + datetime.timedelta(days_ahead)
        target_date2 = target_date1 + datetime.timedelta(days=7)
        target_date3 = target_date2 + datetime.timedelta(days=7)
        target_date4 = target_date3 + datetime.timedelta(days=7)
        target_date5 = target_date4 + datetime.timedelta(days=7)
        target_date_list.append(target_date1)
        target_date_list.append(target_date2)
        target_date_list.append(target_date3)
        target_date_list.append(target_date4)
        target_date_list.append(target_date5)
    return target_date_list


# Creating way to input requested days of week, initializing target_date vars, using the dictionary to associate each day with an index within day_indexes
day_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
day_list = []
day_indexes = []
user = str(input("\nEnter the first name of the user receiving notifications: "))
phone_number = int(input("Enter the 10-digit phone number of the user receiving notifications: "))
phone_number = f"+1{phone_number}"
num_days = int(input("\nEnter the number of days per week for which you'd like to receive tee time notifications\n"
                     "(e.g. If you want only Saturday and Sunday times, input 2) (min: 1, max: 4): "))

restart_day_loop = True
while restart_day_loop:
    restart_day_loop = False
    for i in range(0, num_days):
        ele = str(input(f'Day of Week #{i+1} (Monday-Sunday): '))
        if not (ele == 'Sunday' or ele == 'Monday' or ele == 'Tuesday' or ele == 'Wednesday' or ele == 'Thursday' or
                ele == 'Friday' or ele == 'Saturday'):
            print('\nInvalid day of week entered. Please ensure you are spelling it correctly and capitalizing the '
                  'first letter...\n')
            restart_day_loop = True
            break
        else:
            day_list.append(ele)

for i in day_list:
    a = day_dict[i]
    day_indexes.append(a)

target_1 = 0
target_2 = 0
target_3 = 0
target_4 = 0
target_5 = 0
target_6 = 0
target_7 = 0
target_8 = 0
target_9 = 0
target_10 = 0
target_11 = 0
target_12 = 0
target_13 = 0
target_14 = 0
target_15 = 0
target_16 = 0
target_17 = 0
target_18 = 0
target_19 = 0
target_20 = 0

# Getting user inputs for course selection based upon a given list of courses
course_list = []
num_courses = int(input(f"\nFrom the following list, enter the number of courses that you would like to receive SMS notifications for when tee times go live:\n"
                        f"                    **Please ensure exact spelling as seen here within the following prompts**                                   \n"
                        f""                                                                               
                        f"\nAurora Golf Courses\n"
                        f"Broken Tee\n"
                        f"CommonGround\n"
                        f"Denver Golf Courses\n"
                        f"DU Golf Club\n"
                        f"Foothills Recreation District\n"
                        f"Fossil Trace\n"
                        f"Green Valley Ranch\n"
                        f"Hyland Hills\n"
                        f"Indian Tree\n"
                        f"Lakewood Golf Courses\n"
                        f"Raccoon Creek\n"
                        f"Riverdale\n"
                        f"Saddleback\n"
                        f"Thorncreek\n"
                        f"West Woods\n"                      
                        f"\n"
                        f"Enter number of courses: "))

restart_course_loop = True
while restart_course_loop:
    restart_course_loop = False
    for i in range(0, num_courses):
        ele = str(input(f'Course #{i + 1}: '))
        if not (ele == 'Aurora Golf Courses' or ele == 'Lakewood Golf Courses' or ele == 'Denver Golf Courses' or ele == 'West Woods' or ele == 'Hyland Hills' or
                ele == 'Green Valley Ranch' or ele == 'Fossil Trace' or ele == 'Riverdale' or ele == 'Foothills Recreation District' or ele == 'CommonGround'
                or ele == 'Raccoon Creek' or ele == 'DU Golf Club' or ele == 'Indian Tree' or ele == 'Thorncreek' or ele == 'Saddleback' or ele == 'Broken Tee'):
            print('\nInvalid golf course entered. Please ensure you are spelling it correctly as seen from the list above...or you have to start over :/\n')
            restart_course_loop = True
            break
        else:
            course_list.append(ele)

# Tracking the current time with .9 second intervals, making sure I'm sending a request at least once per second, so I don't miss it
program_running = True
print('\nNotification engine started...')
setup_msg = create_setup_notification(user, day_list, course_list)
send_message(setup_msg, phone_number)
print("Initial notification sent...")
while program_running is True:
    curr_time = arrow.utcnow()
    curr_local_time = curr_time.to('local')
    curr_local_time = curr_local_time.datetime
    target_date_lst = target_dates(curr_local_time, day_indexes)
    curr_local_time_str = curr_local_time.strftime("%Y-%m-%d %H:%M:%S")

    if num_days == 1:
        target_1, target_2, target_3, target_4, target_5 = target_date_lst
        target_1 = target_1.replace(hour=0, minute=0, second=0)
        target_2 = target_2.replace(hour=0, minute=0, second=0)
        target_3 = target_3.replace(hour=0, minute=0, second=0)
        target_4 = target_4.replace(hour=0, minute=0, second=0)
        target_5 = target_5.replace(hour=0, minute=0, second=0)
    elif num_days == 2:
        target_1, target_2, target_3, target_4, target_5, target_6, target_7, target_8, target_9, target_10 = target_date_lst
        target_1 = target_1.replace(hour=0, minute=0, second=0)
        target_2 = target_2.replace(hour=0, minute=0, second=0)
        target_3 = target_3.replace(hour=0, minute=0, second=0)
        target_4 = target_4.replace(hour=0, minute=0, second=0)
        target_5 = target_5.replace(hour=0, minute=0, second=0)
        target_6 = target_6.replace(hour=0, minute=0, second=0)
        target_7 = target_7.replace(hour=0, minute=0, second=0)
        target_8 = target_8.replace(hour=0, minute=0, second=0)
        target_9 = target_9.replace(hour=0, minute=0, second=0)
        target_10 = target_10.replace(hour=0, minute=0, second=0)
    elif num_days == 3:
        target_1, target_2, target_3, target_4, target_5, target_6, target_7, target_8, target_9, target_10, target_11, \
            target_12, target_13, target_14, target_15, = target_date_lst
        target_1 = target_1.replace(hour=0, minute=0, second=0)
        target_2 = target_2.replace(hour=0, minute=0, second=0)
        target_3 = target_3.replace(hour=0, minute=0, second=0)
        target_4 = target_4.replace(hour=0, minute=0, second=0)
        target_5 = target_5.replace(hour=0, minute=0, second=0)
        target_6 = target_6.replace(hour=0, minute=0, second=0)
        target_7 = target_7.replace(hour=0, minute=0, second=0)
        target_8 = target_8.replace(hour=0, minute=0, second=0)
        target_9 = target_9.replace(hour=0, minute=0, second=0)
        target_10 = target_10.replace(hour=0, minute=0, second=0)
        target_11 = target_11.replace(hour=0, minute=0, second=0)
        target_12 = target_12.replace(hour=0, minute=0, second=0)
        target_13 = target_13.replace(hour=0, minute=0, second=0)
        target_14 = target_14.replace(hour=0, minute=0, second=0)
        target_15 = target_15.replace(hour=0, minute=0, second=0)
    elif num_days == 4:
        target_1, target_2, target_3, target_4, target_5, target_6, target_7, target_8, target_9, target_10, target_11, \
            target_12, target_13, target_14, target_15, target_16, target_17, target_18, target_19, target_20 = target_date_lst
        target_1 = target_1.replace(hour=0, minute=0, second=0)
        target_2 = target_2.replace(hour=0, minute=0, second=0)
        target_3 = target_3.replace(hour=0, minute=0, second=0)
        target_4 = target_4.replace(hour=0, minute=0, second=0)
        target_5 = target_5.replace(hour=0, minute=0, second=0)
        target_6 = target_6.replace(hour=0, minute=0, second=0)
        target_7 = target_7.replace(hour=0, minute=0, second=0)
        target_8 = target_8.replace(hour=0, minute=0, second=0)
        target_9 = target_9.replace(hour=0, minute=0, second=0)
        target_10 = target_10.replace(hour=0, minute=0, second=0)
        target_11 = target_11.replace(hour=0, minute=0, second=0)
        target_12 = target_12.replace(hour=0, minute=0, second=0)
        target_13 = target_13.replace(hour=0, minute=0, second=0)
        target_14 = target_14.replace(hour=0, minute=0, second=0)
        target_15 = target_15.replace(hour=0, minute=0, second=0)
        target_16 = target_16.replace(hour=0, minute=0, second=0)
        target_17 = target_17.replace(hour=0, minute=0, second=0)
        target_18 = target_18.replace(hour=0, minute=0, second=0)
        target_19 = target_19.replace(hour=0, minute=0, second=0)
        target_20_ = target_20.replace(hour=0, minute=0, second=0)

    if 'Aurora Golf Courses' in course_list:
        # Tee Sheet Creation
        AuroraGolf = TeeSheet("Aurora Golf Courses", "Starting at 8PM, 10 days in advance", datetime.timedelta(days=9, hours=4), 'https://cityofaurora.ezlinksgolf.com/', '+13037391560 [Murphy Creek]')
        target_times = AuroraGolf.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12, target_13, target_14, target_15, target_16, target_17, target_18, target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        AuroraGolf.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4, target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12, target_13, target_14, target_15, target_16, target_17, target_18, target_19, target_20)

    if 'Lakewood Golf Courses' in course_list:
        # Tee Sheet Creation
        LakewoodGolf = TeeSheet("Lakewood Golf Courses", "Starting at 5PM, 7 days in advance", datetime.timedelta(days=6, hours=7), 'https://foxhollow.quick18.com/', '+13039867888 [Fox Hollow]')
        target_times = LakewoodGolf.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12, target_13, target_14, target_15, target_16, target_17, target_18, target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        LakewoodGolf.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4, target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12, target_13, target_14, target_15, target_16, target_17, target_18, target_19, target_20)

    if 'Denver Golf Courses' in course_list:
        # Tee Sheet Creation
        LakewoodGolf = TeeSheet("Denver Golf Courses (Loyalty)", "Starting at 7PM, 14 days in advance", datetime.timedelta(days=13, hours=5), 'https://denverpremier.ezlinksgolf.com/', '+17208653410 [City Park]')
        target_times = LakewoodGolf.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                   target_7, target_8, target_9, target_10, target_11, target_12,
                                                   target_13, target_14, target_15, target_16, target_17, target_18,
                                                   target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        LakewoodGolf.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                  target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                  target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                  target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                  target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                  target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                  target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                  target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                  target_20)

    if 'Riverdale' in course_list:
        # Tee Sheet Creation
        Riverdale = TeeSheet("Riverdale", "Starting at 7PM, 8 days in advance", datetime.timedelta(days=7, hours=18), 'https://riverdale.book.teeitup.golf/', '+13036596700')
        target_times = Riverdale.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                   target_7, target_8, target_9, target_10, target_11, target_12,
                                                   target_13, target_14, target_15, target_16, target_17, target_18,
                                                   target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        Riverdale.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                  target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                  target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                  target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                  target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                  target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                  target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                  target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                  target_20)

    if 'CommonGround' in course_list:
        # Tee Sheet Creation
        CommonGround = TeeSheet("CommonGround (CGA)", "Starting at 6PM, 8 days in advance", datetime.timedelta(days=7, hours=6), 'https://foreupsoftware.com/index.php/booking/18949/673#/teetimes', '+13033401520')
        target_times = CommonGround.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                   target_7, target_8, target_9, target_10, target_11, target_12,
                                                   target_13, target_14, target_15, target_16, target_17, target_18,
                                                   target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        CommonGround.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                  target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                  target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                  target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                  target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                  target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                  target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                  target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                  target_20)

    if 'Broken Tee' in course_list:
        # Tee Sheet Creation
        BrokenTee = TeeSheet("Broken Tee", "Starting at 7:30AM, 8 days in advance", datetime.timedelta(days=7, hours=16, minutes=30), 'https://broken-tee-golf-course.book.teeitup.com/', '+13037622670')
        target_times = BrokenTee.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                   target_7, target_8, target_9, target_10, target_11, target_12,
                                                   target_13, target_14, target_15, target_16, target_17, target_18,
                                                   target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        BrokenTee.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                  target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                  target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                  target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                  target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                  target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                  target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                  target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                  target_20)

    if 'DU Golf Course' in course_list:
        # Tee Sheet Creation
        DUGolf = TeeSheet("DU Golf Course", "Starting at 12AM, 7 days in advance", datetime.timedelta(days=7, hours=0), 'https://sc.cps.golf/UniversityofDenverV3/', '+13034710000')
        target_times = DUGolf.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                   target_7, target_8, target_9, target_10, target_11, target_12,
                                                   target_13, target_14, target_15, target_16, target_17, target_18,
                                                   target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        DUGolf.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                  target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                  target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                  target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                  target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                  target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                  target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                  target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                  target_20)

    if 'Foothills Recreation District' in course_list:
        # Tee Sheet Creation
        FoothillsRec = TeeSheet("Foothills Recreation District", "Starting at 12AM, 10 days in advance", datetime.timedelta(days=10, hours=0), 'https://www.foothillsgolf.org/teetimes/foothills-championship-18/', '+13034092400 [Foothills]')
        target_times = FoothillsRec.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                     target_7, target_8, target_9, target_10, target_11, target_12,
                                                     target_13, target_14, target_15, target_16, target_17, target_18,
                                                     target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        FoothillsRec.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                    target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                    target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                    target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                    target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                    target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                    target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                    target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                    target_20)

    if 'Fossil Trace' in course_list:
        # Tee Sheet Creation
        FossilTrace = TeeSheet("Fossil Trace", "Starting at 12AM, 7 days in advance", datetime.timedelta(days=7, hours=0), 'https://secure.west.prophetservices.com/FossilTraceV3/', '+13032778750')
        target_times = FossilTrace.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                     target_7, target_8, target_9, target_10, target_11, target_12,
                                                     target_13, target_14, target_15, target_16, target_17, target_18,
                                                     target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        FossilTrace.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                    target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                    target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                    target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                    target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                    target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                    target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                    target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                    target_20)

    if 'Green Valley Ranch' in course_list:
        # Tee Sheet Creation
        GVR = TeeSheet("Green Valley Ranch", "Starting at 12AM, 7 days in advance", datetime.timedelta(days=7, hours=0), 'https://secure.west.prophetservices.com/GreenValleyRanchV3/', '+13033713131')
        target_times = GVR.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                     target_7, target_8, target_9, target_10, target_11, target_12,
                                                     target_13, target_14, target_15, target_16, target_17, target_18,
                                                     target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        GVR.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                    target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                    target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                    target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                    target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                    target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                    target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                    target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                    target_20)

    if 'Hyland Hills' in course_list:
        # Tee Sheet Creation
        Hyland = TeeSheet("Hyland Hills", "Starting at 12AM, 7 days in advance", datetime.timedelta(days=7, hours=0, minutes=1), 'https://www.golfhylandhills.com/teetimes/', '+13034286526')
        target_times = Hyland.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                     target_7, target_8, target_9, target_10, target_11, target_12,
                                                     target_13, target_14, target_15, target_16, target_17, target_18,
                                                     target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        Hyland.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                    target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                    target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                    target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                    target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                    target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                    target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                    target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                    target_20)

    if 'Indian Tree' in course_list:
        # Tee Sheet Creation
        IndianTree = TeeSheet("Indian Tree", "Starting at 12AM, 7 days in advance", datetime.timedelta(days=7, hours=0), 'https://indiantree.cps.golf/', '+13034032542')
        target_times = IndianTree.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                     target_7, target_8, target_9, target_10, target_11, target_12,
                                                     target_13, target_14, target_15, target_16, target_17, target_18,
                                                     target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        IndianTree.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                    target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                    target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                    target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                    target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                    target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                    target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                    target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                    target_20)

    if 'Raccoon Creek' in course_list:
        # Tee Sheet Creation
        RaccoonCreek = TeeSheet("Raccoon Creek", "Starting at 12AM, 14 days in advance", datetime.timedelta(days=14, hours=0), 'https://raccooncreek.ezlinksgolf.com/', '+13039734653')
        target_times = RaccoonCreek.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                         target_7, target_8, target_9, target_10, target_11, target_12,
                                                         target_13, target_14, target_15, target_16, target_17, target_18,
                                                         target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        RaccoonCreek.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                    target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                    target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                    target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                    target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                    target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                    target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                    target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                    target_20)

    if 'Saddleback' in course_list:
        # Tee Sheet Creation
        Saddleback = TeeSheet("Saddleback", "Starting at 12AM, 8 days in advance", datetime.timedelta(days=8, hours=0), 'https://saddleback.cps.golf/', '+13038335000')
        target_times = Saddleback.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                         target_7, target_8, target_9, target_10, target_11, target_12,
                                                         target_13, target_14, target_15, target_16, target_17, target_18,
                                                         target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        Saddleback.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                    target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                    target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                    target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                    target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                    target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                    target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                    target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                    target_20)

    if 'Thorncreek' in course_list:
        # Tee Sheet Creation
        Thorn = TeeSheet("Thorncreek", "Starting at 12AM, 14 days in advance", datetime.timedelta(days=14, hours=0), 'https://thorncreek.quick18.com/', '+13034507055')
        target_times = Thorn.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                                         target_7, target_8, target_9, target_10, target_11, target_12,
                                                         target_13, target_14, target_15, target_16, target_17, target_18,
                                                         target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        Thorn.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                                    target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                                    target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                                    target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                                    target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                                    target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                                    target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                                    target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                                    target_20)

    if 'West Woods' in course_list:
        # Tee Sheet Creation
        Thorn = TeeSheet("West Woods", "Starting at 8AM, 7 days in advance", datetime.timedelta(days=6, hours=16), 'https://www.westwoodsgolf.com/teetimes', '+17208987370')
        target_times = Thorn.get_send_times(num_days, target_1, target_2, target_3, target_4, target_5, target_6,
                                            target_7, target_8, target_9, target_10, target_11, target_12,
                                            target_13, target_14, target_15, target_16, target_17, target_18,
                                            target_19, target_20)
        target_1_comp_str, target_2_comp_str, target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str, target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str, target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str, target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str, target_19_comp_str, target_20_comp_str = target_times
        Thorn.send_trigger(phone_number, num_days, curr_local_time_str, target_1_comp_str, target_2_comp_str,
                           target_3_comp_str, target_4_comp_str, target_5_comp_str, target_6_comp_str,
                           target_7_comp_str, target_8_comp_str, target_9_comp_str, target_10_comp_str,
                           target_11_comp_str, target_12_comp_str, target_13_comp_str, target_14_comp_str,
                           target_15_comp_str, target_16_comp_str, target_17_comp_str, target_18_comp_str,
                           target_19_comp_str, target_20_comp_str, target_1, target_2, target_3, target_4,
                           target_5, target_6, target_7, target_8, target_9, target_10, target_11, target_12,
                           target_13, target_14, target_15, target_16, target_17, target_18, target_19,
                           target_20)

    time.sleep(.97)
    continue
