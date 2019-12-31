#! /home/mefath5/.local/bin/python3
print("Content-Type: text/plain\n")


import sys
import json
import mysql.connector


try:

    data = json.load(sys.stdin)
    email = data["email"]

    connection = mysql.connector.connect(host='localhost',
                                         database='mefath5_mefathim',
                                         user='mefath5_dev',
                                         password='dev12345')

    sql_select_quary = "SELECT * FROM `users` WHERE `email` LIKE '{}'".format(email)
    cursor = connection.cursor()
    cursor.execute(sql_select_quary)
    records = cursor.fetchall()
    
    if records:
        print("this email already exsist")
    else:
        pass
except json.JSONDecodeError as exc:
    print('Failed to decode JSON request: {}'.format(exc))
