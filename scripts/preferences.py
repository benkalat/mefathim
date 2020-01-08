#!/home/mefath5/.local/bin/python3
# print("Content-Type: text/plain; charset=UTF-8\n\n")

import os, cgi, codecs
import mysql.connector
import datetime
import sys
import functions

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

try:

    sid = functions.get_cookie_value('LoggedIn')

    db = functions.connect()

    session_sql = "SELECT `uid`, `update_time`, `logged_out` FROM sessions WHERE sid = '" + sid + "'"

    time_before = (datetime.datetime.now() - datetime.timedelta(minutes=10))

    session_cursor = db.cursor()
    session_cursor.execute(session_sql)
    session = session_cursor.fetchall()

    uid, time, logged = session[0]

    if time > time_before and logged == 0:

        functions.update_connection(sid)

        details_user_dict = {}

        form = cgi.FieldStorage()
        details_user_dict["first_name"] = form.getvalue("first_name")
        details_user_dict["middle_name"] = form.getvalue("middle_name")
        details_user_dict["last_name"] = form.getvalue("last_name")
        details_user_dict["nick_name"] = form.getvalue("nick_name")
        details_user_dict["gender"] = str(form.getvalue("gender"))
        details_user_dict["date_of_birth"] = form.getvalue("birth_date")
        details_user_dict["city"] = form.getvalue("city")
        details_user_dict["country"] = form.getvalue("country")
        details_user_dict["phone_number"] = form.getvalue("phone")

        for x in details_user_dict:
            if details_user_dict[x] is None:
                details_user_dict[x] = ""

        try:
            connection = functions.connect()

            sql_insert_Query = "UPDATE users SET first_name='" + details_user_dict["first_name"] + "',middle_name='" + \
                               details_user_dict["middle_name"] + "',last_name='" + details_user_dict[
                                   "last_name"] + "',nickname='" + details_user_dict["nick_name"] + "',gender='" + \
                               details_user_dict["gender"] + "',date_of_birth='" + details_user_dict[
                                   "date_of_birth"] + "',city='" + details_user_dict["city"] + "',country='" + \
                               details_user_dict["country"] + "',phone_number='" + details_user_dict[
                                   "phone_number"] + "' WHERE id = '" + str(uid) + "'"

            cursor = connection.cursor()
            cursor.execute(sql_insert_Query)
            connection.commit()
            print("location: ../preferences.html?msg=1")
            print("")

        except:
            print("faild")
    else:
        print("location: ../login.html")
        print("")

except mysql.connector.Error as error:
    print(str(error))
