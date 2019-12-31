#!/home/mefath5/.local/bin/python3
import sys
import cgi
import hashlib

import json

import mefath5_connect
print ("Content-Type: text/plain\n")
print ("")

def get_hash(password, salt):
    pwd_salt = str(password)+salt
    m = hashlib.sha1(pwd_salt.encode())
    return m.hexdigest()

# get users input
form = cgi.FieldStorage()
e_mail =  form.getvalue('email')
password =  form.getvalue('password')

mydb = mefath5_connect.get_connect()

if e_mail is None:
	print( "Email cannot be empty" );
	sys.exit()

#sql = f"SELECT salt, password_hash, email FROM users WHERE email = '{e_mail}'"
sql = "SELECT salt, password_hash, email FROM users WHERE email = '" + e_mail + "'"
mycursor =mydb.cursor()

mycursor.execute(sql)
try:
    user_detiles = mycursor.fetchone()
    print("שלום ", user_detiles[2])
except:
    print(e_mail, "! אינך רשום במערכת")

print("<br>")


salt = user_detiles[0]


password_hash = get_hash(password, salt)

if (password_hash == user_detiles[1]):
    print("אתה רשום!!!!!")
    print("<meta http-equiv='refresh' content='5;url=../login.html' />")
else:
    print("סיסמא שגויה נסה שוב!!!")




