"""Define the Student class and its academic information."""
class Student:
    """Class representing a student with academic records, grades, and status flags."""

    def __init__(self, student_id: str, name: str):
        """Initialize a student with a validated ID, name, empty grades, and default statuses."""
        if not str(student_id).strip():
            raise ValueError("Error: Student ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Error: Student name cannot be empty.")

        self.student_id = str(student_id).strip()
        self.name = name.strip()
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grades(self, g: float):
        """Add a numeric grade within the range 0 to 100."""
        if not isinstance(g, (int, float)) or isinstance(g, bool):
            print(f"Error: Invalid grade '{g}'. Grade must be a number.")
            return

        if not 0 <= g <= 100:
            print(f"Error: Grade {g} is out of bounds. Must be between 0 and 100.")
            return

        self.grades.append(float(g))
        self._update_statuses()

    def remove_grade_by_index(self, index: int) -> bool:
        """Remove a grade by its 0-based index position."""
        try:
            if not isinstance(index, int) or isinstance(index, bool):
                raise TypeError("Index must be an integer.")
            removed_value = self.grades.pop(index)
            print(f"Successfully removed grade {removed_value} at index {index}.")
            self._update_statuses()
            return True
        except (IndexError, TypeError):
            print(f"Error: Index {index} is invalid or out of range.")
            return False

    def remove_grade_by_value(self, value: float) -> bool:
        """Remove the first occurrence of a grade matching the given value."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            print(f"Error: Invalid grade value '{value}'. Must be a number.")
            return False

        target = float(value)
        if target in self.grades:
            self.grades.remove(target)
            print(f"Successfully removed grade {target}.")
            self._update_statuses()
            return True
        else:
            print(f"Error: Grade value {target} not found in student's grades.")
            return False

    def calculate_average(self) -> float:
        """Calculate and return the numerical average of all grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self) -> str:
        """Determine the letter grade based on the current average."""
        avg = self.calculate_average()
        if not self.grades:
            return "N/A"
        elif avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def _update_statuses(self):
        """Internal helper method to sync pass/fail and honor roll flags."""
        avg = self.calculate_average()
        self.is_passed = bool(self.grades and avg >= 60)
        self.honor = bool(self.grades and avg >= 90)

    def report(self):
        """Print a structured summary report of the student's information and status."""
        avg = self.calculate_average()
        letter_grade = self.get_letter_grade()
        pass_status = "Passed" if self.is_passed else "Failed"
        honor_status = "Yes" if self.honor else "No"

        print("\n" + "=" * 35)
        print("       STUDENT SUMMARY REPORT     ")
        print("=" * 35)
        print(f" Student ID     : {self.student_id}")
        print(f" Student Name   : {self.name}")
        print(f" Grades List    : {self.grades if self.grades else 'No grades recorded'}")
        print(f" Grades Count   : {len(self.grades)}")
        print(f" Average Grade  : {avg:.2f}")
        print(f" Letter Grade   : {letter_grade}")
        print(f" Pass/Fail      : {pass_status}")
        print(f" Honor Roll     : {honor_status}")
        print("=" * 35)


def main():
    """Demonstrate code functionality against all core and extended requirements."""

    student = Student("S101", "Christian Palma")
    student.add_grades(95.0)
    student.add_grades(72.5)
    student.add_grades(100)

    student.remove_grade_by_value(72.5)
    student.remove_grade_by_index(0)

    print("\n--- Final Student Summary Report ---")
    student.report()


if __name__ == "__main__":
    main()
