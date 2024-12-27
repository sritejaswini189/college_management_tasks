from student import Student

class FacultyMenu:
    def __init__(self, management):
        self.management = management

    def menu(self):
        fid = int(input("Enter Faculty ID: "))
        faculty = self.management.find_faculty(fid)
        if not faculty:
            print("No faculty with this ID!")
            return

        while True:
            print("\t---Faculty Options-----")
            print("1. Add Student", "2. Show Students", "3. Exit", sep="\n")
            opt = int(input("Enter your option: "))
            if opt == 1:
                sid = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                marks = int(input("Enter Marks: "))
                student = Student(sid, name, marks)
                faculty.add_student(student)
                print("Student added successfully!")
            elif opt == 2:
                faculty.show_students()
            elif opt == 3:
                break
            else:
                print("Invalid option!")
