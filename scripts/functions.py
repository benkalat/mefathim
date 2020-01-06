#!/home/mefath5/.local/bin/python3

import mysql.connector
import os
import string
import hashlib
import random


def get_cookie_value(key):
    handler = {}
    if 'HTTP_COOKIE' in os.environ:
        cookies = os.environ['HTTP_COOKIE']
        cookies = cookies.split('; ')

        for cookie in cookies:
            cookie = cookie.split('=')
            handler[cookie[0]] = cookie[1]
    if key in handler:
        return handler[key]
    else:
        return False


def connect():
    db = mysql.connector.connect(host="localhost",
                                 user="mefath5_dev",
                                 password="dev12345",
                                 database="mefath5_mefathim")
    return db


# From https://stackoverflow.com/posts/19213271/revisions
def random_sequence(size):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def get_hash(password, salt):
    pwd_salt = str(password) + str(salt)
    m = hashlib.sha1(pwd_salt.encode())
    return m.hexdigest()