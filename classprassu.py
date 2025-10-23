class Student:

    """A simple class to represent a student."""

    
    def __init__(self, name):
        """
        Initializes the student_name instance variable.
        'self' refers to the newly created object.
        """
       
        self.student_name = name
        print(f"A new Student object for {self.student_name} has been created.")

    
    def display_name(self):
        """
        Displays the student's name using the instance variable.
        """
        print(f"Student Name: {self.student_name}")

 name
student1 = Student("lakshmi")


student2 = Student("prasanna")


print("\nAccessing instance method:")
student1.display_name()
student2.display_name()


print("\nDirectly accessing instance variable:")
print(f"Student 1's Name (direct access): {student1.student_name}")






print(f"Student 2's Name (direct access): {student2.student_name}")
