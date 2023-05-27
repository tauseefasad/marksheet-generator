#MARKSHEET GENERATOR - MTA

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.marks = []

    def add_marks(self, marks):
        self.marks = marks

    def calculate_grade(self):
        # Calculate total and average subject marks
        total = sum(self.marks)
        subject_avg = total / len(self.marks)

        # Check if marks are within the valid range
        if subject_avg < 0 or subject_avg > 100:
            return "Total Marks Invalid"

        # Determine grade and remark based on average subject marks
        if subject_avg >= 90:
            grade = "A"
            remark = "Brilliant"
        elif subject_avg >= 80:
            grade = "B"
            remark = "Good Job"
        elif subject_avg >= 70:
            grade = "C"
            remark = "Did Good"
        elif subject_avg >= 60:
            grade = "D"
            remark = "Need Hard working"
        elif subject_avg >= 50:
            grade = "E"
            remark = "Put all efforts"
        else:
            grade = "F"
            remark = "You can do better than this"

        # Calculate CGPA based on grade
        if grade == "A":
            cgpa = 4.0
        elif grade == "B":
            cgpa = 3.0
        elif grade == "C":
            cgpa = 2.0
        elif grade == "D":
            cgpa = 1.0
        elif grade == "E":
            cgpa = 0.5
        else:
            cgpa = 0.0

        return {
            "Total Marks": total,
            "Average Grade": grade,
            "Remark": remark,
            "CGPA": cgpa
        }


def main():
    name = input("Enter name: ")
    number = int(input("Enter ID number: "))

    student = Student(name, number)

    print("Enter Obtained Marks of 5 subjects: ")
    marks = []
    for i in range(5):
        marks.append(int(input()))

    student.add_marks(marks)
    grade_info = student.calculate_grade()

    print("===========")
    for key, value in grade_info.items():
        print(key + ":", value)
    print("Student Details- ")
    print("Student Name:", student.name)
    print("Student Identity Number:", student.number)


# Execute the main function
main()
