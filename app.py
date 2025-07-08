from student import register, list_student
from auth import login
def main():
    if not login():
         print("Login fail")
         return
    while True:
            print("\nStudent Management System\n")
            print("Press 1 for register")
            print("Press 2 for list students")
            print("press 3 for exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                 register()
            elif choice == '2':
                 list_student()
            elif choice == '3':
                 print("BYE")
                 break

 
if __name__ == '__main__':
    main()
