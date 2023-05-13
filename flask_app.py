from flask import Flask, request
import pandas as pd
from twilio.twiml.messaging_response import MessagingResponse

user_acct_tbl = pd.DataFrame(columns=["ID", "PHONE_NUM", "FIRST_NAME", "HAS_DAY_LIST", "DAY_LIST", "HAS_COURSE_LIST", "COURSE_LIST"])
app = Flask(__name__)


@app.route('/sms/', methods=['POST'])
def incoming_sms():
    """Get the text of an incoming text message, apply logic based on what is contained in the user account table"""
    # Get the message the user sent our Twilio number
    body = str(request.values.get('Body', None))
    phone_num = str(request.values.get('From'))

    resp = MessagingResponse()

    def response_and_check(bdy, phn_num, response_var):
        global user_acct_tbl
        if bdy == "Begin":
            if len(user_acct_tbl) == 1:
                user_list = user_acct_tbl["ID"].squeeze()
                if int(phn_num[2:]) != user_list:
                    new_phone_num = phn_num
                    new_id = int(phn_num[2:])
                    new_df = pd.DataFrame({'ID': [new_id], 'PHONE_NUM': [new_phone_num], 'FIRST_NAME': [""], 'HAS_DAY_LIST': [False], "DAY_LIST": [""], "HAS_COURSE_LIST": [False], 'COURSE_LIST': [""]})
                    user_acct_tbl = pd.concat([user_acct_tbl, new_df])
                    response_var.message(f"Welcome to 303-Weekender. Please respond to the following prompts to choose your settings:")
                elif int(phn_num[2:]) == user_list:
                    response_var.message(f"You are already subscribed to 303-Weekender. Respond with STOP to unsubscribe")
            else:
                user_series = user_acct_tbl["ID"].squeeze()
                user_list = user_series.tolist()
                if int(phn_num[2:]) not in user_list:
                    new_phone_num = phn_num
                    new_id = int(phn_num[2:])
                    new_df = pd.DataFrame({'ID': [new_id], 'PHONE_NUM': [new_phone_num], 'FIRST_NAME': [""], 'HAS_DAY_LIST': [False], "DAY_LIST": [""], "HAS_COURSE_LIST": [False], 'COURSE_LIST': [""]})
                    user_acct_tbl = pd.concat([user_acct_tbl, new_df])
                    response_var.message(f"Welcome to 303-Weekender. Please respond to the following prompts to choose your settings:")
                elif int(phn_num[2:]) in user_list:
                    response_var.message(f"You are already subscribed to 303-Weekender. Respond with STOP to unsubscribe")
        user_acct_tbl_index = user_acct_tbl.set_index('ID')
        new_id = int(phn_num[2:])
        if user_acct_tbl_index.at[new_id, 'FIRST_NAME'] == "":
            response_var.message(f"What is your first name?")

    response_and_check(body, phone_num, resp)

    return str(resp)


if __name__ == '__main__':
    app.run(port=5000)