# person_module.py

from datetime import date

class Person:
    """
    A class used to represent a person with basic biographical attributes 
    and a method to calculate their age.
    """

    def __init__(self, name: str, country: str, dob: date):
        """
        Initializes the Person class with name, country, and date of birth.

        :param name: The person's full name (e.g., "Alan Turing").
        :param country: The person's country of origin (e.g., "UK").
        :param dob: The person's date of birth as a datetime.date object.
        """
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self) -> int:
        """
        Calculates the person's current age based on their DOB.

        The calculation uses today's date and subtracts 1 from the year 
        difference if the birthday for the current year hasn't occurred yet.
        
        :return: The person's age in full years.
        """
        today = date.today()
        
        # Calculate the base age as the difference in years
        age = today.year - self.dob.year
        
        # Check if the birthday has passed this year. 
        # If today's date is before the birthday month/day, subtract 1 from age.
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
            
        return age

    def get_info(self) -> str:
        """Returns a string summary of the person's information."""
        return (f"{self.name} ({self.country}) is currently "
                f"{self.calculate_age()} years old.")

# End of person_module.py
