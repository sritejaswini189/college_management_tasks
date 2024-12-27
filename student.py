class Student:
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks

class StudentMenu:
    def __init__(self, management):
        self.management = management

    def menu(self):
        sid = int(input("Enter Student ID: "))
        student = self.find_student(sid)
        if not student:
            print("No student with this ID!")
            return

        while True:
            print("\t---Student Options-----")
            print("1. Show Marks", "2. Exit", sep="\n")
            opt = int(input("Enter your option: "))
            if opt == 1:
                print(f"ID: {student.sid}\nName: {student.name}\nMarks: {student.marks}")
            elif opt == 2:
                break
            else:
                print("Invalid option!")

    def find_student(self, sid):
        for faculty in self.management.faculty_list:
            for student in faculty.students:
                if student.sid == sid:
                    return student
        return None
