#!/home/mefath5/.local/bin/python3
print("Content-Type: text/plain; charset=UTF-8\n\n")

import os, codecs
import datetime
import sys, json
import functions

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

try:
    sid = functions.get_cookie_value('LoggedIn')
    if not sid:
        json_res = {"ok": False, "data": []}
        print(json.dumps(json_res, indent=4, default=str, ensure_ascii=False).encode('utf-8').decode())
        sys.exit()

    db = functions.connect()

    session_sql = "SELECT `uid`, `update_time`, `logged_out` FROM sessions WHERE sid = '" + sid + "'"

    time_before = (datetime.datetime.now() - datetime.timedelta(minutes=10))

    session_cursor = db.cursor()
    session_cursor.execute(session_sql)
    session = session_cursor.fetchall()

    uid, time, logged = session[0]
    checker = True
    user = {}
    if time > time_before and logged == 0:

        functions.update_connection(sid)

        data_sql = "SELECT `email`, `first_name`, `middle_name`, `last_name`, `nickname`, `gender`, `date_of_birth`, `city`, `country`, `phone_number` FROM `users` WHERE id = '" + str(uid) + "'"

        mycursor = db.cursor()
        mycursor.execute(data_sql)
        data = mycursor.fetchall()

        list_of_columens = [i[0] for i in mycursor.description]
        for row in data:
            user = {key: val for key, val in zip(list_of_columens, row)}

        for x in user:
            if user[x] == None:
                user[x] = ""

    else:
        checker = False
    json_res = {"ok": checker, "data": user}
    print(json.dumps(json_res, indent=4, default=str, ensure_ascii=False).encode('utf-8').decode())

except Exception as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
