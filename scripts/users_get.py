#!/home/mefath5/.local/bin/python3

import functions
import json
import os
import sys
import codecs
import datetime

# Note this line. It's the important one
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/plain; charset=UTF-8\n\n")

try:

    sid = functions.get_cookie_value('LoggedIn')
    if not sid:
        json_res = {"ok": False, "data": []}
        print(json.dumps(json_res, indent=4, default=str, ensure_ascii=False).encode('utf-8').decode())
        sys.exit()

    mydb = functions.connect()

    session_sql = "SELECT `update_time`, `logged_out` FROM sessions WHERE sid = '" + sid + "'"

    mycursor = mydb.cursor()
    mycursor.execute(session_sql)
    details = mycursor.fetchall()

    time_before = (datetime.datetime.now() - datetime.timedelta(minutes=10))
    time, logged = details[0]

    checker = True
    users = []

    if time > time_before and logged == 0:

        functions.update_connection(sid)

        time_before = (datetime.datetime.now() - datetime.timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S')

        session_sql = "SELECT `uid` FROM `sessions` WHERE logged_out = 0 AND update_time >= '" + time_before + "'"
        mycursor.execute(session_sql)
        ids = mycursor.fetchall()

        # clean the result and covert it to a tuple
        new_ids = tuple([item[0] for item in ids])
        if len(new_ids) > 1:
            sql = "SELECT nickname FROM users WHERE id in {}".format(new_ids)
        else:
            sql = "SELECT nickname FROM users WHERE id LIKE {}".format(new_ids[0])
        mycursor.execute(sql)
        all_details = mycursor.fetchall()

        list_of_columens = [i[0] for i in mycursor.description]
        for row in all_details:
            user = {key: val for key, val in zip(list_of_columens, row)}
            users.append(user)
    else:
        checker = False
    json_res = {"ok": checker, "data": users}
    print(json.dumps(json_res, indent=4, default=str, ensure_ascii=False).encode('utf-8').decode())

except Exception as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
