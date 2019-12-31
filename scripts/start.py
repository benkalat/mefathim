#!/home/mefath5/.local/bin/python3
# print("Content-Type: text/plain\n")

import os
import sys
import mysql.connector
import datetime

try:

    handler = {}
    if 'HTTP_COOKIE' in os.environ:
        cookies = os.environ['HTTP_COOKIE']
        cookies = cookies.split('; ')

        for cookie in cookies:
            cookie = cookie.split('=')
            handler[cookie[0]] = cookie[1]

    got_cookie = False

    for k in handler:
        if k == "LoggedIn":
            sid = handler[k]
            got_cookie = True

    if not got_cookie:
        print("location: ../login.html\n")
        print("")
        sys.exit()

    #print ("Content-Type: text/plain")
    #print ("")
    #print("1")
    db = mysql.connector.connect(host="localhost",
                                   user="mefath5_dev",
                                   password="dev12345",
                                   port=3306,
                                   database="mefath5_mefathim")
    #print("2")
    sql = "SELECT `update_time`, `logged_out` FROM sessions WHERE sid = '" + sid + "'" 

    #print(sql)
    time_before = (datetime.datetime.now() - datetime.timedelta(minutes=10))

    #print("4")
    session_cursor = db.cursor()
    session_cursor.execute(sql)

    #print("5")
    session = session_cursor.fetchall()

    # print(session[0])
    time, logged = session[0]

    #print("6")
    if time > time_before and logged == 0:
        print("location: ../users_get.html\n")
    else:
        print("location: ../login.html\n")
		
    print("")

except Exception as e:
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print(exc_type, fname, exc_tb.tb_lineno)

