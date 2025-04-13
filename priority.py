student={}

def add(name,grade,attendance):
    student[name]=(grade,attendance)
    print(f"{name} is added")

def remove(name):
    del student[name]
    print(f"{name} is removed")

def update(name,grade,attendance):
    if name in student:
        student[name]=(grade,attendance)
        print("Grade & attendance updated")
    else:
        print("No student found")

def display_sorted():
    sorted_students = sorted(student.items(), key=lambda x: (-x[1][0], -x[1][1]))

    print("\nSorted Student List (by grade & attendance):")
    for name, (grade, attendance) in sorted_students:
        print(f"{name}: Grade = {grade}, Attendance = {attendance}%")



x=True
while x:

    print("Enter the operation you want to perform")
    print("1.Add a student")
    print("2.Remove a student")
    print("3.Update a student")
    print("4.Display all students")
    print("5.Exit")

    a=int(input())

    if(a==1):
        name=input("Add student name")
        grade=int(input("Add student's grade"))
        attendance=int(input("Add student's attendance"))
        add(name,grade,attendance)

    elif(a==2):
        name=input("Add student name")
        remove(name)

    elif(a==3):
        name=input("Add student name")
        grade=int(input("Add student's grade"))
        attendance=int(input("Add student's attendance"))
        update(name,grade,attendance)
    
    elif(a==4):
        display_sorted()

    elif(a==5):
        print("Exited.")
        x=False
