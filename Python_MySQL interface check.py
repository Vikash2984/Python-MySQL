import mysql.connector as c
con = c.connect(host = 'localhost', user = 'root', password = 'Lk#12142597', database = 'test')
if con.is_connected():
    print("Successfully connected....")
