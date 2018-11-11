from my_sqlite3 import *
from my_display import *
from my_class import *
from my_attendance import *
from read_rfid import *



def add_card():                             # function to add TAG NAME ID
    try:
        r_1 = read_card()
        add_data_database(r_1)
    except:
        print('Could not Add card Try Again ')


def main():
    display()
    while True:
        command=input('Enter Your choice ')
        if command == "1":
            add_card()

        if command == "2":
            delete_database()

        if command == "3":
            read_database()

        if command == "4":
            attendance()

        if command == "5":
            break
        if command == "6":
            pass


if __name__ == '__main__':
    main()
