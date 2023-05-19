from flask import Flask, request
import pandas as pd
from twilio.twiml.messaging_response import MessagingResponse
import user_db


def list_validity(ipt, valid_list):
    if ', ' in ipt:
        lst = ipt.split(', ')
    else:
        lst = ipt.split(',')
    for i in lst:
        if i in valid_list:
            continue
        else:
            return "Fail"
    return lst


def style_list(lst):
    length = len(lst)
    if length == 1:
        return lst[0]
    elif length == 2:
        return f"{lst[0]} & {lst[1]}"
    else:
        return ", ".join(lst[:-1]) + f", & {lst[-1]}"


app = Flask(__name__)


@app.route('/sms/', methods=['POST'])
def incoming_sms():
    """Get the text of an incoming text message, apply logic based on what is contained in the user account table"""
    # Get the message the user sent our Twilio number
    body = str(request.values.get('Body', None))
    phone_num = str(request.values.get('From'))

    resp = MessagingResponse()

    def response_and_check(bdy, phn_num, response_var):
        # "Begin" logic
        begin_str = "Begin"
        begin_no_case = begin_str.casefold()
        bdy_no_case = bdy.casefold()
        if bdy_no_case == begin_no_case:
            if len(user_db.user_acct_tbl) == 1:
                user_list = user_db.user_acct_tbl["ID"].squeeze()
                if int(phn_num[2:]) != user_list:
                    new_phone_num = phn_num
                    new_id = int(phn_num[2:])
                    new_df = pd.DataFrame({'ID': [new_id], 'PHONE_NUM': [new_phone_num], 'FIRST_NAME': [""], 'HAS_DAY_LIST': [0], "DAY_LIST": [""], "HAS_COURSE_LIST": [0], 'COURSE_LIST': [""], 'ACTIVE': [0]})
                    user_db.user_acct_tbl = pd.concat([user_db.user_acct_tbl, new_df])
                    response_var.message(f"Welcome to 303-Weekender. Please respond to the following prompts to choose your settings:")
                elif int(phn_num[2:]) == user_list:
                    response_var.message(f"You are already subscribed to 303-Weekender. Respond with STOP to unsubscribe")
            else:
                user_series = user_db.user_acct_tbl["ID"].squeeze()
                user_list = user_series.tolist()
                if int(phn_num[2:]) not in user_list:
                    new_phone_num = phn_num
                    new_id = int(phn_num[2:])
                    new_df = pd.DataFrame({'ID': [new_id], 'PHONE_NUM': [new_phone_num], 'FIRST_NAME': [""], 'HAS_DAY_LIST': [0], "DAY_LIST": [""], "HAS_COURSE_LIST": [0], 'COURSE_LIST': [""], 'ACTIVE': [0]})
                    user_db.user_acct_tbl = pd.concat([user_db.user_acct_tbl, new_df])
                    response_var.message(f"Welcome to 303-Weekender. Please respond to the following prompts to choose your settings:")
                elif int(phn_num[2:]) in user_list:
                    response_var.message(f"You are already subscribed to 303-Weekender. Respond with STOP to unsubscribe")

        # Creating phone number index from user account table, using it for lookups
        user_acct_tbl_index = user_db.user_acct_tbl.set_index('ID')
        new_id = int(phn_num[2:])

        if user_acct_tbl_index.index.isin([new_id]).any():
            # Config logic
            config_str = "Config"
            config_str = config_str.casefold()
            if bdy_no_case == config_str:
                user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] = 0
                user_acct_tbl_index.at[new_id, 'DAY_LIST'] = ""
                user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] = 0
                user_acct_tbl_index.at[new_id, 'COURSE_LIST'] = ""
                user_acct_tbl_index.at[new_id, 'ACTIVE'] = 0
                user_db.update_user_acct_table(user_acct_tbl_index)

            # Getting the responses from the text, converting those responses for use in the program and rejecting responses that don't fit, storing the user information in the user account table
            if user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] == 0 and user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 1 and bdy_no_case != begin_no_case and bdy_no_case != config_str:
                valid_course_list = ["Aurora Golf Courses", "Broken Tee", "CommonGround", "Denver Golf Courses", "DU Golf Club", "Foothills Recreation District", "Fossil Trace", "Green Valley Ranch", "Hyland Hills", "Indian Tree", "Lakewood Golf Courses", "Raccoon Creek", "Riverdale", "Saddleback", "Thorncreek", "West Woods"]
                course_list_valid = list_validity(str(bdy), valid_course_list)
                if course_list_valid != "Fail":
                    user_acct_tbl_index.at[new_id, 'COURSE_LIST'] = course_list_valid
                    user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] = 1
                    user_db.update_user_acct_table(user_acct_tbl_index)
                else:
                    response_var.message(f"Invalid response. One or more courses from the course list were entered incorrectly.")
            if user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 0 and user_acct_tbl_index.at[new_id, 'FIRST_NAME'] != "" and bdy_no_case != begin_no_case and bdy_no_case != config_str:
                valid_day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                day_list_valid = list_validity(str(bdy), valid_day_list)
                if day_list_valid != "Fail":
                    user_acct_tbl_index.at[new_id, 'DAY_LIST'] = day_list_valid
                    user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] = 1
                    user_db.update_user_acct_table(user_acct_tbl_index)
                else:
                    response_var.message(f"Invalid response. Please ensure you are entering the day of the week with proper capitalization.")
            if user_acct_tbl_index.at[new_id, 'FIRST_NAME'] == "" and bdy_no_case != begin_no_case and bdy_no_case != config_str:
                user_acct_tbl_index.at[new_id, 'FIRST_NAME'] = str(bdy)
                user_db.update_user_acct_table(user_acct_tbl_index)

            # Sending the prompts to the user once tasks have been completed
            if user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 1 and user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] == 0:
                response_var.message(f"From the following list, enter the courses that you would like to receive SMS notifications for, separated by commas, when tee times go live:")
                response_var.message(f"(Please ensure exact spelling as seen here within the following prompts)")
                response_var.message(f"Aurora Golf Courses\n"
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
                                     f"West Woods")
            if user_acct_tbl_index.at[new_id, 'FIRST_NAME'] != "" and user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 0:
                response_var.message(f"Hi {user_acct_tbl_index.at[new_id, 'FIRST_NAME']}, provide the days of the week you want tee times on, separated by commas. You can select up to four days.\n"
                                     f"\n"
                                     f'(ex. "Friday, Sunday")')
            if user_acct_tbl_index.at[new_id, 'FIRST_NAME'] == "":
                response_var.message(f"What is your first name?")

            # Sending subscription notification
            if user_acct_tbl_index.at[new_id, 'FIRST_NAME'] != "" and user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 1 and user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] == 1:
                if user_acct_tbl_index.at[new_id, 'ACTIVE'] == 0:
                    response_var.message(f'Congrats. You are now set to receive notifications for {style_list(user_acct_tbl_index.at[new_id, "DAY_LIST"])} tee times at the following courses: {style_list(user_acct_tbl_index.at[new_id, "COURSE_LIST"])}.\n'
                                         f'\n'
                                         f"Respond 'config' to change your notification settings\n"
                                         f"Respond 'unsub' to unsubscribe")
                user_acct_tbl_index.at[new_id, 'ACTIVE'] = 1
                user_db.update_user_acct_table(user_acct_tbl_index)

            # Unsub logic
            if user_acct_tbl_index.at[new_id, 'ACTIVE'] == 1:
                unsub_str = "Unsub"
                unsub_str = unsub_str.casefold()
                if bdy_no_case == unsub_str:
                    user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] = 0
                    user_acct_tbl_index.at[new_id, 'DAY_LIST'] = ""
                    user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] = 0
                    user_acct_tbl_index.at[new_id, 'COURSE_LIST'] = ""
                    user_acct_tbl_index.at[new_id, 'ACTIVE'] = 0
                    user_db.update_user_acct_table(user_acct_tbl_index)
                    response_var.message('You are now unsubscribed. Respond with anything to re-subscribe.')
        else:
            response_var.message('Invalid response. Please subscribe first.')

    response_and_check(body, phone_num, resp)

    return str(resp)


if __name__ == '__main__':
    app.run(port=5000)
