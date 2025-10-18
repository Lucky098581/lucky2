class Person:
    
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
class Student(Person):
    def __init__(self,name,age,rollno = 278):
        super().__init__(name,age)

    def introduce(self):
        print(f"My name is {self.name},Age is{self.Age},roll number{self.roll_no}.")

obj = Student("Lakshmi",20)
obj.introduce()
