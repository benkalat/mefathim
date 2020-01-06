#!/home/mefath5/.local/bin/python3

import os
import sys
import datetime
import functions

try:
    sid = functions.get_cookie_value('LoggedIn')

    db = functions.connect()

    time_logged_out = datetime.datetime.now()
    time_logged_out = str(time_logged_out)

    sql = "UPDATE `sessions` SET `logged_out`= 1, `logout_time`='" + time_logged_out + "' WHERE sid = '" + sid + "'"

    session_cursor = db.cursor()
    session_cursor.execute(sql)

    db.commit()
    db.close()

    print("location: ../login.html\n\n")

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
