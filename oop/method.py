class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

# Create a student object
my_student = Student("Alice")

# Display the student's name
my_student.display()