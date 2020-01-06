#!/home/mefath5/.local/bin/python3

import json
import sys
import codecs
import functions

print("Content-Type: text/plain\n\n")

# Note this line. It's the important one
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


try:

    data = json.load(sys.stdin)
    email = data["email"]

    connection = functions.connect()

    sql_select = "SELECT * FROM `users` WHERE `email` LIKE '" + email + "'"
    cursor = connection.cursor()
    cursor.execute(sql_select)
    records = cursor.fetchall()

    if records:
        print("האימייל הזה כבר קיים")
    else:
        pass
except json.JSONDecodeError as exc:
    print('Failed to decode JSON request: {}'.format(exc))
