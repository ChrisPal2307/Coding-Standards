"""Define the Student class and its academic information."""
class Student:
    """Class representing a student with an ID, name, and grades."""
    def __init__(self, student_id, name):
        """Initialize a student with an ID, name, and empty grades."""
        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.student_id = student_id
        self.name = name.strip()
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grades(self, g):
        """Add a grade to the student's list of grades."""
        if not isinstance(g, (int, float)):
            raise ValueError("Invalid grade type. Grade must be a number.")
        self.grades.append(g)

    def calculate_average(self):
        """Calculate and return the average of the grades."""
        t = 0
        for x in self.grades:
            t += x
        avg = t / len(self.grades) if self.grades else 0
        return avg

    def check_honor(self):
        """Check if the student qualifies for honors based on their average grade."""
        if self.calculate_average() > 90:
            self.honor = True
        else:
            self.honor = False

    def delete_grade(self, index):
        """Delete a grade from the student's list of grades."""
        if index < 0 or index >= len(self.grades):
            raise IndexError("Index out of range")
        del self.grades[index]

    def report(self):  # broken format
        """Print a report of the student's information and grades."""
        print("Student Report:")
        print(" ID: " + self.student_id)
        print(" Name is: " + self.name)
        print(" Grades Count: " + str(len(self.grades)))
        print(" Final Grade = " + str(self.calculate_average()))


def startrun():
    """Run a series of tests on the student class."""
    a = Student("x", "Christian Palma")
    a.add_grades(100)
    a.add_grades(50)  # broken
    a.calculate_average()
    a.check_honor()
    a.delete_grade(1)  # IndexError
    a.report()


startrun()
