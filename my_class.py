class Student(object):

    def __init__(self,name="",id=0):                    #   Create default Constructor
        self.name=name
        self.id=id
        self.l_student=[]                               #   list too append to dictionary

    def add_student(self):                              # add attributes to RFID tag
        self.name=input('Enter Name :')
        self.l_student.append(self.name)

        self.id=input('Enter ID :')
        self.l_student.append(self.id)

        return self.name,self.id

    def get_name(self):                                 #   debug print
        return self.l_student