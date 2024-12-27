from management import Management
from faculty import FacultyMenu
from student import StudentMenu

class HomeMenu:
    def __init__(self):
        self.management = Management()

    def menu(self):
        while True: 
            print("\t-----Available Logins-----",
                  "1. Management", "2. Faculty", "3. Student", "4. Exit", sep="\n")
            login = int(input("Enter your login option: "))
            if login == 1:
                self.management_menu()
            elif login == 2:
                FacultyMenu(self.management).menu()
            elif login == 3:
                StudentMenu(self.management).menu()
            elif login == 4:
                print("<--------Exiting-------->")
                break
            else:
                print("Invalid option!")

    def management_menu(self):
        while True:
            print("\t---Management Options-----")
            print("1. Add Faculty", "2. Show Faculty", "3. Exit", sep="\n")
            opt = int(input("Enter your option: "))
            if opt == 1:
                fid = int(input("Enter Faculty ID: "))
                name = input("Enter Faculty Name: ")
                print(self.management.add_faculty(fid, name))
            elif opt == 2:
                self.management.show_faculty()
            elif opt == 3:
                break
            else:
                print("Invalid option!")

if __name__ == "__main__":
    HomeMenu().menu()
