#q1. Mini Utility Project: Create a command-line utility to calculate student grades using dictionaries and loops.

class Student:
    def __init__(self):
        self.students=[]
    def add_student(self):
        name=input("Enter Student Name: ")
        marks=int(input("Enter Student's marks: "))
        self.students.append({"name":name,"marks":marks})
        print("Student details added Successfully")
    def show_student_details(self):
        for student in self.students:
            if student["marks"]>=90:
                student["grade"]="A"
            elif student["marks"]>=80 and student["marks"]<90:
                student["grade"]="B"
            elif student["marks"]>=70 and student["marks"]<80:
                student["grade"]="C"
            elif student["marks"]>=60 and student["marks"]<70:
                student["grade"]="D"
            elif student["marks"]>=50 and student["marks"]<60:
                student["grade"]="E"
            else:
                student["grade"]="F"
        counter=1
        for student in self.students:
            print(f"{counter}) Name: {student["name"]}, Marks: {student["marks"]}, Grade: {student["grade"]}")
            counter+=1
student=Student()
while True:
    print("Enter 1 to add student details")
    print("Enter 2 to see student details")
    print("Enter any other number to exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        student.add_student()
    elif choice==2:
        student.show_student_details()
    else:
        print("Exiting...")
        break


