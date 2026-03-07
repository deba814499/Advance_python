# college cgpa

class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def enter_marks(self):
        for i in range(5):
            m = int(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(m)

    def calculate_result(self):
        total = sum(self.marks)
        percentage = total / 5
        gpa = percentage / 10
        return total, percentage, gpa

    def display_result(self):
        total, percentage, gpa = self.calculate_result()

        print("\n----- Result -----")
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)
        print("Total:", total)
        print("Percentage:", percentage)
        print("GPA:", round(gpa,2))


# Main Program
name = input("Enter student name: ")
roll = input("Enter roll number: ")

s = Student(name, roll)

s.enter_marks()
s.display_result()