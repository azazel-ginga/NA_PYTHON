#coding=utf-8
'''
编写一个学生类，提供name、age、gender、phone、address、email等属性。为学生提供带所有成员变量的构造器，为学生提供方法，用于描绘吃、喝、玩、乐
'''

class Classroom(object):
    num = 0

    @classmethod
    def addnum(cls):
        cls.num = cls.num + 1

    @classmethod
    def getnum(cls):
        return cls.num

    def __new__(cls):
        Classroom.addnum()
        return super().__new__(cls)

class Student(Classroom):
    def __init__(self):
        self.name = ''
        self.gender = ''
        self.phone = ''
        self.address = ''
        self.email = ''


    @property
    def inputname(self):
        return self.name

    @inputname.setter
    def inputname(self,name):
        if is_number(name):
            print('The name can not contain number!')
        else:
            self.name = name


    def getgender(self):
        return self.gender

    def setgender(self,gender):
        if (gender == 'MALE') or (gender == 'FEMALE'):
            self.gender = gender
        else:
            print('Please input "FEMALE" or "MALE"')

    gender = property(getgender,setgender)


s1 = Student()
s1.inputname = 'AAA'
s1.gender = 'MALE'
#s2 = Student()
print(Classroom.getnum())


