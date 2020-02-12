#!/home/mefath5/.local/bin/python3

import cgi, sys, codecs,os
import json
import mefath5_connect
try:
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    print ("Content-type: text/plain; charset=UTF-8\n\n")


    mydb = mefath5_connect.get_connect()
    cursor = mydb.cursor()


    def print_posts():
        select_query = "SELECT post_id, user_name,post_text,write_time FROM posts ORDER BY post_id DESC LIMIT 5 "
        cursor.execute(select_query)
        post_data = cursor.fetchall()

        json_data=[]
        for x in post_data:
            user = x[1]
            json_data.append({"post" : x[0], "user" : user,"text" : x[2],"writing_time": x[3],})

        data = json.dumps(json_data, indent=4, default=str, ensure_ascii=False).encode('UTF-8')
        print(data.decode())


    print_posts()
except Exception as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)


