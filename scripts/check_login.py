#!/home/mefath5/.local/bin/python3

import cgi, sys, codecs
import os
import hashlib
import json
import string
import random
import datetime
import mefath5_connect


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) 

def random_cookie():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(10))

def get_hash(password, salt):
    pwd_salt = str(password)+salt
    m = hashlib.sha1(pwd_salt.encode())
    return m.hexdigest()

def write_to_file(data):
    with open('../json/user_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
            

try:
    # get users input
    form = cgi.FieldStorage()
    e_mail = form.getvalue('email')
    password = form.getvalue('password')
    mydb = mefath5_connect.get_connect()
    
    if e_mail is None:
        print ("location: ../login.html?err=1")
        print("")
    
    sql = "SELECT salt, password_hash, first_name, id FROM users WHERE email = '" + e_mail + "'"
    mycursor =mydb.cursor()
    
    mycursor.execute(sql)
    try:
        user_details = mycursor.fetchone()
        salt = user_details[0]
        password_hash = get_hash(password, salt)
        user_name = user_details[2]
        if (password_hash == user_details[1]):
            
            json_data = {"email" : e_mail, "name" : user_name}
            write_to_file(json_data)
            
            # OK, password correct, create a cookie, find the ip + user_agent, save it in the data base, and set-cookie(sid:cookie)
            user_ip = os.environ["REMOTE_ADDR"]
            user_agent = os.environ["HTTP_USER_AGENT"]
            cookie_id = random_cookie()
            user_id = str(user_details[3])
            update_time = str(datetime.datetime.now())
            # Set a Cookie at the Browser
            print("Set-Cookie: LoggedIn="+cookie_id+";path=/")
            
            # Insert data into the sessions table
            insert_query = "INSERT INTO sessions ( sid, uid, ip_address, user_agent, update_time ) VALUES ('"+ cookie_id +"','"+ user_id +"','"+ user_ip +"','"+ user_agent +"','"+ update_time +"')"
            
            mycursor.execute(insert_query)
            mydb.commit()
            
            # Now, go to home page...
            print ("location: ../users_get.html")
            print("")
        else:
            print ("location: ../login.html?err=1")
            print("")
    except:
        print ("location: ../login.html?err=1")
        print("")
    finally:
        mydb.close()

        
except BaseException as e:
    print('Failed to do something: ' + str(e))