import mysql.connector

def get_connect():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="mefath5_dev",
        password ="dev12345",
        database ="mefath5_mefathim")
    return mydb