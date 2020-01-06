#!/home/mefath5/.local/bin/python3

import cgi
import functions
import random
import datetime
import sys
import os

try:

    form = cgi.FieldStorage()
    salt = random.randint(1000, 9999)
    password = form.getvalue("password")
    password_again = form.getvalue("password_again")
    if password != password_again:
        print('location: ../sign_up.html?err=1\n')

    currnet_date = datetime.datetime.now()

    email = form.getvalue("email")
    first_name = form.getvalue("first_name")
    middle_name = form.getvalue("middle_name")
    last_name = form.getvalue("last_name")
    status = str(0)
    nick_name = form.getvalue("nick_name")
    salt = salt
    password = functions.get_hash(password, salt)
    create_date = str(currnet_date)
    gender = str(form.getvalue("gender"))
    date_of_birth = form.getvalue("birth_date")
    city = form.getvalue("city")
    country = form.getvalue("country")
    phone_number = form.getvalue("phone")

    if nick_name == "":
        nick_name = first_name

    try:
        connection = functions.connect()

        sql_insert_Query = "INSERT INTO users (email, first_name, middle_name, last_name, status, nickname, salt, password_hash, creation_date, gender, date_of_birth, city, country, phone_number)VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(email, first_name, middle_name, last_name, status, nick_name, salt, password, create_date, gender, date_of_birth, city, country, phone_number)

        cursor = connection.cursor()
        cursor.execute(sql_insert_Query)
        connection.commit()

        print("location: ../login.html?msg=2&email=" + email + "\n")
        cursor.close()

    except:
        print("Content-Type: text/plain\n")

    finally:
        if connection.is_connected():
            connection.close()

except BaseException as e:
    print('Failed to do something: ' + str(e))
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)