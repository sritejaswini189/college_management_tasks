class Faculty:
    def __init__(self, fid, name):
        self.fid = fid
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        if not self.students:
            print("No students")
        else:
            for student in self.students:
                print(f"ID-- {student.sid}\tName-- {student.name}")

class Management:
    def __init__(self):
        self.faculty_list = []

    def add_faculty(self, fid, name):
        self.faculty_list.append(Faculty(fid, name))
        return "Faculty added successfully!"

    def show_faculty(self):
        if not self.faculty_list:
            print("No faculty registered.")
        else:
            for faculty in self.faculty_list:
                print(f"ID--- {faculty.fid}\tName--- {faculty.name}")

    def find_faculty(self, fid):
        for faculty in self.faculty_list:
            if faculty.fid == fid:
                return faculty
        return None
