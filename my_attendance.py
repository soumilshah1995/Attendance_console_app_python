import sqlite3
import time
from read_rfid import *
from my_sqlite3 import *
import datetime
import serial
import time
from my_display import *
m=[]


def attendance_database(tag_my, name_my, id_my, my_time):
    # Create a new data base
    conn_my=sqlite3.connect('My_DataBase.db')
    c_my = conn_my.cursor()
    c_my.execute('CREATE TABLE IF NOT EXISTS attendance (Tag TEXT,Name TEXT,Id TEXT,record TEXT)')
    c_my.execute("INSERT INTO attendance (Tag, Name, Id, record) VALUES (?, ?, ?, ?)",(tag_my, name_my, id_my, my_time))
    conn_my.commit()
    c_my.close()
    conn_my.close()


def attendance():
    l = []
    conn=sqlite3.connect('My_DataBase.db')
    c=conn.cursor()
    c.execute('SELECT * FROM my_student')
    for x in c.fetchall():
        l.append(x[6])
        print(l)

    print ('Attendance system place your card !')

    while True:
        r=read_card()
        if r in l:
            c.execute('SELECT * FROM my_student WHERE Tag=? ', (r,))
            data=c.fetchall()
            print ('{} present'.format(data))

            tag_my= data[0][0]
            name_my= data[0][1]
            id_my= data[0][2]
            my_time = datetime.datetime.time(datetime.datetime.now())

            #my_time=datetime.datetime.now()
            #my_time = datetime.datetime.time(datetime.datetime.now())
            #my_date = str(datetime.datetime.today()).split()[0]

            attendance_database(tag_my, name_my, id_my, my_time)
            print (tag_my,name_my,id_my,time)

