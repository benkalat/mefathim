#!/home/mefath5/.local/bin/python3

import cgi
import functions
import os
import sys
import random

try:
    
    # get the users value 
    form = cgi.FieldStorage()

    e_mail = form.getvalue('email')
    old_password = form.getvalue('old_password')
    password = form.getvalue('password1')
    password2 = form.getvalue('password2')

    if e_mail is None:
        print("location: ../change_password.html?err=1&msg="+e_mail+"\n")
    if old_password is None:
        print("location: ../change_password.html?err=1&msg="+e_mail+"\n")
    if password is None:
        print("location: ../change_password.html?err=1&msg="+e_mail+"\n")
    if password2 is None:
        print("location: ../change_password.html?err=1&msg="+e_mail+"\n")
    if password != password2:
        print("location: ../change_password.html?err=1&msg="+e_mail+"\n")

    mydb = functions.connect()
    mycursor = mydb.cursor()

    # check if the temporary password is true
    sql = "SELECT salt, password_hash FROM users WHERE email = '" + e_mail + "'"
    mycursor.execute(sql)

    try:
        user_details = mycursor.fetchone()
    except:
        print("location: ../change_password.html?err=0\n")

    old_salt = user_details[0]
    old_password_hash = functions.get_hash(old_password, old_salt)

    if old_password_hash == user_details[1]:

        salt = str(random.randint(1000, 9999))
        password_hash = functions.get_hash(password, salt)

        sql = "UPDATE users SET salt = '" + salt + "', password_hash='" + password_hash + "' WHERE email = '" + e_mail + "' "

        try:
            mycursor.execute(sql)
            mydb.commit()
            # All is OK, return "password changed" msg.
            print("location: ../login.html?msg=0&email="+e_mail)
            print("")
            
        except:
            print("location: ../change_password.html?err=1&msg="+e_mail)
            print("")
    else:
        print("location: ../change_password.html?err=1&msg="+e_mail)
        print("")
    mydb.close()

except BaseException as e:
    print("location: ../change_password.html?err=1&msg="+str(e))
    print("")
    print('Failed to do something: ' + str(e))
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)