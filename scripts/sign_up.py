#!/home/mefath5/.local/bin/python3

import cgi
import hashlib
import mysql.connector
import random
import datetime
import json
import sys
import os

try:

	print("Content-Type: text/plain\n")
	print("")

	print("qwertyu")

	form = cgi.FieldStorage()

	salt = random.randint(1000, 9999)

	password = form.getvalue("password")

	new_password = str(password) + str(salt)
	m = hashlib.sha1(new_password.encode())

	currnet_date = datetime.datetime.now()

	email = form.getvalue("email")
	first_name = form.getvalue("first_name")
	middle_name = form.getvalue("middle_name")
	last_name = form.getvalue("last_name")
	status = str(0)
	nick_name = form.getvalue("nick_name")
	salt = salt
	password = str(m.hexdigest())
	create_date = str(currnet_date)
	gender = str(form.getvalue("gender"))
	date_of_birth = form.getvalue("birth_date")
	city = form.getvalue("city")
	country = form.getvalue("country")
	phone_number = form.getvalue("phone")

	data = {
		"email": email,
		"first_name": first_name,
		"middle_name": middle_name,
		"last_name": last_name,
		"nickname": nick_name,
		"password": password,
		"date_of_birth": date_of_birth,
		"city": city,
		"country": country,
		"phone_number": phone_number
	}

	j_data = json.dumps(data, ensure_ascii=False).encode('utf8')

	try:
		# print("Before connect")
		connection = mysql.connector.connect(host='localhost',
											 database='mefath5_mefathim',
											 user='mefath5_dev',
											 password='dev12345')


		# print( "After connect" )
		
		sql_insert_Query = "INSERT INTO users (email, first_name, middle_name, last_name, status, nickname, salt, password_hash, creation_date, gender, date_of_birth, city, country, phone_number)VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(email, first_name, middle_name, last_name, status, nick_name, salt, password, create_date, gender, date_of_birth, city, country, phone_number)
		
		# print( sql_insert_Query )
		cursor = connection.cursor()
		cursor.execute(sql_insert_Query)
		connection.commit()

		print(j_data.decode())
		cursor.close()

	except mysql.connector.Error as error:
		print(str(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed")

except BaseException as e:
    print('Failed to do something: ' + str(e) )	
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)