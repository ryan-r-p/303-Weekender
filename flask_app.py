from flask import Flask, request
import pandas as pd
from twilio.twiml.messaging_response import MessagingResponse
import user_db

pd.set_option('display.max_colwidth', None)

app = Flask(__name__)


@app.route('/sms/', methods=['POST'])
def incoming_sms():
    """Get the text of an incoming text message, apply logic based on what is contained in the user account table"""
    # Get the message the user sent our Twilio number
    body = str(request.values.get('Body', None))
    phone_num = str(request.values.get('From'))

    resp = MessagingResponse()

    def response_and_check(bdy, phn_num, response_var):
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

        user_acct_tbl_index = user_db.user_acct_tbl.set_index('ID')
        new_id = int(phn_num[2:])

        if user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] == 0 and user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 1:
            user_acct_tbl_index.at[new_id, 'COURSE_LIST'] = str(bdy)
            user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] = 1
            user_db.update_user_acct_table(user_acct_tbl_index)
        if user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 0 and user_acct_tbl_index.at[new_id, 'FIRST_NAME'] != "":
            user_acct_tbl_index.at[new_id, 'DAY_LIST'] = str(bdy)
            user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] = 1
            user_db.update_user_acct_table(user_acct_tbl_index)
        if user_acct_tbl_index.at[new_id, 'FIRST_NAME'] == "" and bdy_no_case != begin_no_case:
            user_acct_tbl_index.at[new_id, 'FIRST_NAME'] = str(bdy)
            user_db.update_user_acct_table(user_acct_tbl_index)

        if user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 1 and user_acct_tbl_index.at[new_id, 'HAS_COURSE_LIST'] == 0:
            response_var.message(f"Blah blah blah: here's the course list and a couple newlines\n"
                                 f"\n"
                                 f"Tee-hee")
        if user_acct_tbl_index.at[new_id, 'FIRST_NAME'] != "" and user_acct_tbl_index.at[new_id, 'HAS_DAY_LIST'] == 0:
            response_var.message(f"Hi {user_acct_tbl_index.at[new_id, 'FIRST_NAME']}, provide the days of the week you want tee times on, separated by commas. You can select up to four days.\n"
                                 f"\n"
                                 f'(ex. "Friday, Sunday")')
        if user_acct_tbl_index.at[new_id, 'FIRST_NAME'] == "":
            response_var.message(f"What is your first name?")
        print(user_db.user_acct_tbl.to_string())

    response_and_check(body, phone_num, resp)

    return str(resp)


if __name__ == '__main__':
    app.run(port=5000)
