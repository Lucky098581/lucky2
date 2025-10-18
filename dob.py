from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob


    def calculate_age(self):
        today = date.today()
        age = today.year-self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age-=1
        return age

Person1 = Person("lakshmi prasanna","ongole",date(2006,9,19))

print("calculated age for each person")
print("***************************")
print("Person 1:")
print("Name:",Person1.name)
print("Country:",Person1.country)
print("dob:",Person1.dob)
print("age:",Person1.calculate_age())

