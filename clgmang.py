class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Student(Person):
    def __init__(self, id, name, marks):
        super().__init__(id, name)
        self.marks = marks


class Faculty(Person):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.students = []  

    def add_student(self, student):
        self.students.append(student)
        return f"Student {student.name} added successfully!"

    def show_students(self):
        if not self.students:
            print("No students")
        else:
            for student in self.students:
                print(f"ID: {student.id} \tName: {student.name}")


class Management:
    def __init__(self):
        self.faculties = []  
        self.management_ids = [5, 7, 9]

    def add_faculty(self, id, name):
        self.faculties.append(Faculty(id, name))
        return "Faculty added successfully!"

    def show_faculties(self):
        if not self.faculties:
            print("No faculties")
        else:
            for faculty in self.faculties:
                print(f"ID: {faculty.id} \tName: {faculty.name}")

    def find_faculty_by_id(self, id):
        for faculty in self.faculties:
            if faculty.id == id:
                return faculty
        return None


class CollegeSystem:
    def __init__(self):
        self.management = Management()
        self.students = [] 

    def find_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def home_login(self):
        while True:
            print("\t-----Available Logins-----")
            print("1.Management\n2.Faculty\n3.Student\n4.Exit")
            login = int(input("Enter the login: "))
            if login == 1:
                self.management_login()
            elif login == 2:
                self.faculty_login()
            elif login == 3:
                self.student_login()
            elif login == 4:
                print("<--------Exiting-------->")
                break
            else:
                print("Invalid option")

    def management_login(self):
        mId = int(input("Enter ID: "))
        while True:
            if mId in self.management.management_ids:
                print("\t---Management Options-----")
                print("1.Add Faculty\n2.Show Faculty\n3.Exit")
                opt = int(input("Enter your option: "))
                if opt == 1:
                    id = int(input("Enter ID: "))
                    name = input("Enter name: ")
                    print(self.management.add_faculty(id, name))
                elif opt == 2:
                    self.management.show_faculties()
                elif opt == 3:
                    break
                else:
                    print("Invalid option")
            else:
                print("!!!Unauthorized access!!!")
                mId = int(input("Enter ID: "))

    def faculty_login(self):
        fId = int(input("Enter ID: "))
        while True:
            faculty = self.management.find_faculty_by_id(fId)
            if faculty:
                print("\t---Faculty Options-----")
                print("1.Add Student\n2.Show Students\n3.Exit")
                opt = int(input("Enter your option: "))
                if opt == 1:
                    id = int(input("Enter ID: "))
                    name = input("Enter name: ")
                    marks = int(input("Enter Marks: "))
                    student = Student(id, name, marks)
                    self.students.append(student)
                    print(faculty.add_student(student))
                elif opt == 2:
                    faculty.show_students()
                elif opt == 3:
                    break
                else:
                    print("Invalid option")
            else:
                print("!!!No faculty with this ID!!!")
                fId = int(input("Enter ID: "))

    def student_login(self):
        sId = int(input("Enter ID: "))
        while True:
            student = self.find_student_by_id(sId)
            if student:
                print("\t---Student Options-----")
                print("1.Show Marks\n2.Exit")
                opt = int(input("Enter your option: "))
                if opt == 1:
                    print("---Details-----")
                    print(f"ID: {student.id}\nName: {student.name}")
                    print(f"Subject: Computer Science\nMarks: {student.marks}")
                elif opt == 2:
                    break
                else:
                    print("Invalid option")
            else:
                print("!!!No student with this ID!!!")
                sId = int(input("Enter ID: "))
college_system = CollegeSystem()
college_system.home_login()
