#!/home/mefath5/.local/bin/python3

import mysql.connector
import json
import os
import sys
import codecs

# Note this line. It's the important one
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/plain\n")

try:

    sql = "SELECT * FROM users"

    mydb = mysql.connector.connect(host="localhost",
                                  user="mefath5_dev",
                                  password="dev12345",
                                  database="mefath5_mefathim")

    mycursor = mydb.cursor()
    mycursor.execute(sql)

    all_details = mycursor.fetchall()

    list_of_columens = [i[0] for i in mycursor.description]
    users = []

    for row in all_details:
        user = {key: val for key, val in zip(list_of_columens, row)}
        users.append(user)

    print(json.dumps(users, indent=4, default=str, ensure_ascii=False).encode('utf-8').decode())

except Exception as e:
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print(exc_type, fname, exc_tb.tb_lineno)



