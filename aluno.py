import uuid

class Person:
    def __init__(self, name, age):
        self.studentID = uuid.uuid1()
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course, grade):
        super().__init__(name,age)
        self.course = course
        self.grade = grade

    def __repr__(self):
        return f'''\nStudent ID: {self.studentID} \n 
Name: {self.name} \n 
Age: {self.age} \n 
Course: {self.course} \n 
Grade: {self.grade} \n '''

if __name__ == '__main__':
    student = Student('Fernando', 19, 'Javascript', 10)
    print(student)