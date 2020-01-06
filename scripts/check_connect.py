#!/home/mefath5/.local/bin/python3

import json
import sys, os
import codecs
import functions
import datetime

print("Content-Type: text/plain\n\n")

# Note this line. It's the important one
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


try:

    data = json.load(sys.stdin)

    cookie = data["cookie"]
    time_before = (datetime.datetime.now() - datetime.timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S')

    connection = functions.connect()

    sql_select = "SELECT * FROM `sessions` WHERE `sid` LIKE '" + cookie + "' AND logged_out = 0 AND update_time >= '" + time_before + "'"

    cursor = connection.cursor()
    cursor.execute(sql_select)
    records = cursor.fetchall()

    if records:
        connect = True
    else:
        connect = False
        
    json_res = {'ok': connect}
    print(json.dumps(json_res, indent=4, default=str, ensure_ascii=False).encode('utf-8').decode())

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
