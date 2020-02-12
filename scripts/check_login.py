#!/home/mefath5/.local/bin/python3

import cgi, sys, codecs
import datetime
import functions
import os

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

try:
    # get users input
    form = cgi.FieldStorage()
    e_mail = form.getvalue('email')
    password = form.getvalue('password')
    mydb = functions.connect()
    
    if e_mail is None:
        print("location: ../login.html?err=1")
        print("")
    
    sql = "SELECT salt, password_hash, id FROM users WHERE email = '" + e_mail + "'"
    mycursor = mydb.cursor()
    mycursor.execute(sql)

    try:
        user_details = mycursor.fetchone()
        salt = user_details[0]
        password_hash = functions.get_hash(password, salt)

        if password_hash == user_details[1]:
            # OK, password correct, create a cookie, find the ip + user_agent, save it in the data base, and set-cookie(sid:cookie)
            user_ip = os.environ["REMOTE_ADDR"]
            user_agent = os.environ["HTTP_USER_AGENT"]
            cookie_id = functions.random_sequence(10)
            user_id = str(user_details[2])
            update_time = str(datetime.datetime.now())

            # Insert data into the sessions table
            insert_query = "INSERT INTO `sessions`(`sid`, `uid`, `create_time`, `update_time`, `ip_address`, `user_agent`) VALUES ('" + cookie_id + "','" + user_id + "','" + update_time + "','" + update_time + "','" + user_ip + "','" + user_agent + "')"

            mycursor.execute(insert_query)
            mydb.commit()
            mydb.close()

            print("Set-Cookie: LoggedIn=" + cookie_id + "; Path=/")

            # Now, go to home page...
            print("location: ../home_page.html")
            print("")
        else:
            print("location: ../login.html?err=1")
            print("")
    except:
        print("location: ../login.html?err=1")
        print("")

except BaseException as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)