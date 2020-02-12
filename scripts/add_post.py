#!/home/mefath5/.local/bin/python3

import cgi, sys, codecs, os
import json
import mefath5_connect

try:
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    print ("Content-type: text/plain; charset=UTF-8\n\n")

    def add_post():
        insert_query = "INSERT INTO posts (user_name, post_text) VALUES ('"+ user_name +"', '"+ text +"')"
        cursor.execute(insert_query)
        mydb.commit()

    form = cgi.FieldStorage()
    # back_color = form.getvalue('back_color')
    text = form.getvalue('text')
    # text_color = form.getvalue('text_color')
    # font_type = form.getvalue('font_type')
    # font_size = form.getvalue('font_size')

    mydb = mefath5_connect.get_connect()
    cursor = mydb.cursor()

    handler = {}
    if 'HTTP_COOKIE' in os.environ:
        cookies = os.environ['HTTP_COOKIE']
        cookies = cookies.split('; ')
        #print (cookies)

        for cookie in cookies:
            cookie = cookie.split('=')
            handler[cookie[0]] = cookie[1]

    for k in handler:
        if k == "LoggedIn":
            sid = handler[k]
    #print(sid)
    # sid = "1qOaiEn3Fs"
    id_query = "SELECT uid FROM sessions WHERE sid= '" + sid +"'"
    cursor.execute(id_query)
    user_id = cursor.fetchone()
    print (user_id)
    print ("47")
    data_query = "SELECT first_name FROM users WHERE id = '" + str(user_id[0]) + "'"
    cursor.execute(data_query)
    user_name = cursor.fetchone()
    user_name = user_name[0]
    print (type(user_name))
    add_post()

except Exception as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
# print(back_color, text, text_color, font_size, font_type)
