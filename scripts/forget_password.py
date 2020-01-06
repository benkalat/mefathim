#!/home/mefath5/.local/bin/python3

import sys, codecs
import cgi
import smtplib
import random
import functions
import os

# Note this line. It's for hebrew printing on the screen
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


# Create a new random password and hash it - return: (new password, salt, hashed password)
def new_password():
    # Create a new password
    size = random.randint(8, 12)
    new_pwd = functions.random_sequence(size)
    salt = random.randint(1000, 9999)
    # Hash them
    hash_pwd = functions.get_hash(new_pwd, salt)
    return new_pwd, str(salt), hash_pwd

try:
    # Prefer the data
    pwd, salt, hash_pwd = new_password()
    form = cgi.FieldStorage()
    sent_to = form.getvalue('email')

    if sent_to is None:
        print("location: ../forget_password.html?err=1\n")

    # print(type(salt), type(hash_pwd), type(sent_to))

    mydb = functions.connect()
    sql = "UPDATE users SET salt = '" + salt + "', password_hash='" + hash_pwd + "' WHERE email = '{}'".format(sent_to)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(sql)
        mydb.commit()
    except:
        print("location: ../forget_password.html?err=1\n")

    # If the email is correct, send an email with a new message
    if mycursor.rowcount > 0:

        # From https://github.com/JayRizzo/Random_Scripts/blob/master/sendgmail.py
        sent_from = 'mefathim2@gmail.com'
        gmail_app_password = 'pointertopointer'
        sent_subject = 'איפוס סיסמא'
        sent_body = ("\n\n"+"הסיסמא הזמנית שלך היא:\n" + pwd + "\n\n"+"https://mefathim.com/login.html?msg=2&email=" + sent_to + "\n" + " הכנסו לאתר מפתחים\n")
        email_text = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n %s"
        % (sent_from, sent_to, sent_subject, sent_body))
        try:

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(sent_from, gmail_app_password)
            server.sendmail(sent_from, sent_to, email_text.encode('UTF-8'))
            server.close()
            print("location: ../change_password.html?msg={}".format(sent_to))
            print("")

        except BaseException as e:
            print("Content-Type: text/plain\n")
            print('Failed to do something: ' + str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print("location: ../forget_password.html?err=1\n")
    else:
        print("location: ../forget_password.html?err=1\n")
    mydb.close()

except BaseException as e:
    # print('Failed to do something: ' + str(e))
    # exc_type, exc_obj, exc_tb = sys.exc_info()
    # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    # print(exc_type, fname, exc_tb.tb_lineno)
    print("location: ../forget_password.html?err=" + str(e))
    print("")