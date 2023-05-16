import pandas as pd

user_acct_tbl = pd.DataFrame(columns=["ID", "PHONE_NUM", "FIRST_NAME", "HAS_DAY_LIST", "DAY_LIST", "HAS_COURSE_LIST", "COURSE_LIST", "ACTIVE"])


def update_user_acct_table(user_account_tbl_w_indexes):
    global user_acct_tbl
    user_account_tbl_w_indexes = user_account_tbl_w_indexes.reset_index()
    user_acct_tbl = user_account_tbl_w_indexes
