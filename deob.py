from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        """Calculates age in full years only."""
        today = date.today()
        age = today.year - self.dob.year
        
        
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

    def calculate_age_detailed(self):
        """Calculates age in years, months, and days."""
        today = date.today()
        
        diff = (today, self.dob)
        return diff.years, diff.months, diff.days


Person1 = Person("lakshmi prasanna", "ongole", date(2006, 9, 19))


years, months, days = Person1.calculate_age_detailed()

print("Calculated Age for Person 1")
print("***************************")
print("Name:", Person1.name)
print("Country:", Person1.country)
print("DOB:", Person1.dob)
print("---------------------------")
print(f"Age in full years: {Person1.calculate_age()} years")
print(f"Detailed Age: {years} years, {months} months, and {days} days")
