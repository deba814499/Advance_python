class StudentGradeSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, grade):
        try:
            if not student_id:
                raise ValueError("Student ID cannot be empty")

            grade = float(grade)

            if student_id in self.students:
                print("Student already exists.")
            else:
                self.students[student_id] = grade
                print("Student added successfully.")

        except ValueError as e:
            print("Error:", e)

    def update_grade(self, student_id, grade):
        try:
            if student_id not in self.students:
                raise KeyError("Invalid student ID")

            grade = float(grade)
            self.students[student_id] = grade
            print("Grade updated.")

        except ValueError:
            print("Grade must be a number.")
        except KeyError as e:
            print("Error:", e)

    def delete_student(self, student_id):
        try:
            if student_id not in self.students:
                raise KeyError("Invalid student ID")

            del self.students[student_id]
            print("Student deleted.")

        except KeyError as e:
            print("Error:", e)

    def display(self):
        print("\nStudent Records")
        for sid, grade in self.students.items():
            print(sid, ":", grade)


system = StudentGradeSystem()

system.add_student("101", 85)
system.add_student("102", 90)
system.update_grade("101", 88)
system.delete_student("102")
system.display()