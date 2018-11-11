import sqlite3
from my_class import *
from my_main import *


def add_data_database(r_1):
    try:
        r= r_1
        s=Student()
        conn=sqlite3.connect('My_DataBase.db')
        c=conn.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS my_student (Tag TEXT,Name TEXT,Id TEXT)')
        nam, id = s.add_student()
        c.execute("INSERT INTO my_student (Tag, Name, Id) VALUES (?, ?, ?)", (r, nam, id,))
        conn.commit()
        c.close()
        conn.close()
    except:
        print('Could not Add to DataBase ')


def read_database():
    try:
        conn=sqlite3.connect('My_DataBase.db')
        c=conn.cursor()
        c.execute('SELECT * FROM my_student ')
        for x in c.fetchall():
            print(" ", x)
    except:
        print('Could not Read from Database ')


def delete_database():
    try:
        tag=input('enter id')
        conn=sqlite3.connect('My_DataBase.db')
        c=conn.cursor()
        c.execute("DELETE FROM  my_student WHERE Tag=?", (tag,))
        conn.commit()

    except:
        print ('cannot delete database')


def check (r_1):
    l = []
    conn=sqlite3.connect('My_DataBase.db')
    c=conn.cursor()
    c.execute('SELECT * FROM my_student')

    for x in c.fetchall():
        l.append(x[0])
    #print (l)

    conn.commit()
    if r_1 not in l:
        return True
    else:
        # print ('not found')
        return False


