#program to insert reccords in a relation
import mysql.connector as c
con = c.connect(host = 'localhost', user = 'root', password = 'Lk#12142597', database = 'test')

cursor = con.cursor()
while True :
    code = int(input('Enter Student ID : '))
    name = input('Enter your name : ')
    marks = int(input('Enter your marks : '))

    query = "insert into class values({},'{}',{})".format(code,name,marks)

    cursor.execute(query)

    con.commit()
    print("Data inserted successfully...")

    choice = int(input("\n1-> Enter more records \n2-> Exit \nEnter you choice : "))
    if choice == 2:
        break
