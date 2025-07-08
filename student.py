import os
import json
import re

STUDENT_FILE = 'data/students.json'
COURSES = ['BCA','MCA','B.TECH','M.TECH']




def register():
    name = input("Enter your Name: ")
    if not (len(name)>=2 and name.isalpha()):
        print("invalid")
        return
        

    
    reg_no = input("Enter your Registration Number(e.g., REG-2024-0001): ")
    if not re.match(r'^REG-\d{4}-\d{4}$',reg_no):
        print("Invalid format")
        return
    
    try:
        age= int(input("Enter your age: "))
        if age<18 or age>25:
            print("Age must be between 18&25")
            return
    except ValueError:
        print("Invalid")
        return
    
    email = input("Enter your email id: ")
    if not re.match(r'^\S+@\S+\.\S+$',email):
        print("Invalid format")
        return
    
    phone = input("Enter your Phone number: ")
    if not(phone.isdigit() and len(phone)==10):
        print("Invalid")
        return
    
    print("Courses: "," ,".join(COURSES))
    normal_text=[]
    for c in COURSES:
        clean = c.replace('.','').title()
        normal_text.append(clean)
        
    course = input("Enter the Course: ").replace('.','').title()
    if course not in normal_text:
        print("Invalid")
        return
    
 
    
    student = {
        'name':name,
        'reg_no':reg_no,
        'age':age,
        'email':email,
        'phone':phone,
        'course':course
    }

    save_student(student)
    print("Registerd Successfully")

def save_student(student):
    dir_name=os.path.dirname(STUDENT_FILE)
    if dir_name:
        os.makedirs(dir_name,exist_ok=True)
    
    if not os.path.exists(STUDENT_FILE) or os.stat(STUDENT_FILE).st_size == 0:
        with open(STUDENT_FILE,'w') as f:
            json.dump([],f)
    
    with open(STUDENT_FILE,'r+') as f:
        data = json.load(f)
        data.append(student)
        f.seek(0)
        json.dump(data, f, indent=4)


def list_student():
    if not os.path.exists(STUDENT_FILE):
        print("No Registrations yet")
        return
    
    try:
        with open(STUDENT_FILE,'r') as f:
            students = json.load(f)
    except json.JSONDecodeError:
        print("No registartions yet")
        return
    
    
    print("Registered Students\n")
    for i,s in enumerate(students,1):
        print(f"{i}.Name:{s['name']}|Register Number:{s['reg_no']}|Age:{s['age']}|Email:{s['email']}|Phone:{s['phone']}|Course:{s['course']}\n")


    






    


