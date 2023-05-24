import sqlite3
import pandas as pd

cxn = sqlite3.connect('user_data.db', check_same_thread=False)
curs = cxn.cursor()


def create_new_user_db_tbl_if_not_existing():
    query = f"""CREATE TABLE IF NOT EXISTS USER_DB (
                    ID INTEGER PRIMARY KEY,
                    PHONE_NUM TEXT,
                    FIRST_NAME TEXT,
                    HAS_DAY_LIST INTEGER,
                    DAY_LIST_1 TEXT,
                    DAY_LIST_2 TEXT,
                    DAY_LIST_3 TEXT,
                    DAY_LIST_4 TEXT,
                    HAS_COURSE_LIST INTEGER,
                    COURSE_LIST_1 TEXT,
                    COURSE_LIST_2 TEXT,
                    COURSE_LIST_3 TEXT,
                    COURSE_LIST_4 TEXT,
                    COURSE_LIST_5 TEXT,
                    COURSE_LIST_6 TEXT,
                    COURSE_LIST_7 TEXT,
                    COURSE_LIST_8 TEXT,
                    COURSE_LIST_9 TEXT,
                    COURSE_LIST_10 TEXT,
                    ACTIVE INTEGER  
                    )"""
    curs.execute(query)
    cxn.commit()


def query_all_user_data():
    query = "SELECT * FROM USER_DB"
    df = pd.read_sql_query(query, cxn)
    return df


def get_user_course_lists(new_id):
    query = f""" SELECT ID, COURSE_LIST_1 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_1 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_2 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_2 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_3 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_3 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_4 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_4 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_5 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_5 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_6 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_6 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_7 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_7 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_8 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_8 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_9 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_9 IS NOT NULL
    UNION ALL
    SELECT ID, COURSE_LIST_10 AS COURSE_LIST FROM USER_DB WHERE ID = {new_id} AND COURSE_LIST_10 IS NOT NULL
    """
    df = pd.read_sql_query(query, cxn)
    return df


def get_user_day_lists(new_id):
    query = f""" SELECT ID, DAY_LIST_1 AS DAY_LIST FROM USER_DB WHERE ID = {new_id} AND DAY_LIST_1 IS NOT NULL
    UNION ALL
    SELECT ID, DAY_LIST_2 AS DAY_LIST FROM USER_DB WHERE ID = {new_id} AND DAY_LIST_2 IS NOT NULL
    UNION ALL
    SELECT ID, DAY_LIST_3 AS DAY_LIST FROM USER_DB WHERE ID = {new_id} AND DAY_LIST_3 IS NOT NULL
    UNION ALL
    SELECT ID, DAY_LIST_4 AS DAY_LIST FROM USER_DB WHERE ID = {new_id} AND DAY_LIST_4 IS NOT NULL
    """
    df = pd.read_sql_query(query, cxn)
    return df


def insert_id_and_phone_num(new_id, new_phone):
    query = """INSERT INTO USER_DB (ID, PHONE_NUM, HAS_DAY_LIST, HAS_COURSE_LIST, ACTIVE) VALUES (?, ?, 0, 0, 0)"""
    curs.execute(query, (new_id, new_phone))
    cxn.commit()


def insert_first_name(first_name, new_id):
    query = """UPDATE USER_DB SET FIRST_NAME = ? WHERE ID = ?"""
    curs.execute(query, (first_name, new_id))
    cxn.commit()


def insert_day_list(user_day_list, new_id):
    i = 1
    query1 = f"""UPDATE USER_DB SET HAS_DAY_LIST = 1 WHERE ID = ?"""
    curs.execute(query1, (new_id,))
    cxn.commit()
    for day in user_day_list:
        query2 = f"""UPDATE USER_DB SET DAY_LIST_{i} = ? WHERE ID = ?"""
        curs.execute(query2, (day, new_id))
        cxn.commit()
        i += 1


def insert_course_list(user_course_list, new_id):
    i = 1
    query1 = f"""UPDATE USER_DB SET HAS_COURSE_LIST = 1 WHERE ID = ?"""
    curs.execute(query1, (new_id,))
    cxn.commit()
    for course in user_course_list:
        query = f"""UPDATE USER_DB SET COURSE_LIST_{i} = ? WHERE ID = ?"""
        curs.execute(query, (course, new_id))
        cxn.commit()
        i += 1


def set_active(new_id):
    query = f"""UPDATE USER_DB SET ACTIVE = 1 WHERE ID = {new_id}"""
    curs.execute(query)
    cxn.commit()


def enter_config(new_id):
    query = """UPDATE USER_DB SET HAS_DAY_LIST = 0, 
                                  DAY_LIST_1 = NULL,
                                  DAY_LIST_2 = NULL,
                                  DAY_LIST_3 = NULL,
                                  DAY_LIST_4 = NULL,
                                  HAS_COURSE_LIST = 0,
                                  COURSE_LIST_1 = NULL,
                                  COURSE_LIST_2 = NULL,
                                  COURSE_LIST_3 = NULL,
                                  COURSE_LIST_4 = NULL,
                                  COURSE_LIST_5 = NULL,
                                  COURSE_LIST_6 = NULL,
                                  COURSE_LIST_7 = NULL,
                                  COURSE_LIST_8 = NULL,
                                  COURSE_LIST_9 = NULL,
                                  COURSE_LIST_10 = NULL,
                                  ACTIVE = 0
                WHERE ID = ?"""
    curs.execute(query, (new_id,))
    cxn.commit()


def unsub(new_id):
    query = "DELETE FROM USER_DB WHERE ID = ?"
    curs.execute(query, (new_id,))
    cxn.commit()
