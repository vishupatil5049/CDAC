import json
"""
Student Grade Management System
"""
cohort1=[{"id": 1,
          "name": "Ram",
          "course": "Python",
          "marks": 70,
          "grade": "B"}]

id_counter=len(cohort1)
def menu():
    menuText="""    1: Enroll Student
    2: Cohort/View Directory
    3: Query/Search Records
    4: Revise/Update Evaluation
    5: Purge/Delete Record
    6: Save to JSON
    7: Load from JSON
    8: Exit"""
    print(menuText)
    try:
        choice=int(input("Enter choice: "))
    except:
        choice= False
        print("Choice should be integer")
    return choice
#---------------------------------------------------------------------------------------
def enroll():
    global id_counter, cohort1
    print("Add Student Details : ")
    
    name = input("Enter the Name: ").strip().title()
    print(name)
    if not name or name.isnumeric():
        print("Invalid Input")
        return
    
    course = input("Enter the Course / Module : ").strip().title()
    if not course or course.isnumeric():
        print("Invalid Input")
        return
    
    try:
        marks = float(input("Enter the Marks : "))
        if marks < 0.0 or marks > 100.0:
          print("Marks must be between 0.0 and 100.0 ")
          return
        if marks >= 85.0:
            grade="A"
        elif 70.0 <= marks < 85.0:
            grade="B"
        elif 50.0 <= marks < 70.0:
            grade="C"
        else:
            grade="F"
    except ValueError:
        print("Invalid price format. Please enter a number.")
        return
    
    id_counter += 1
    # record=dict([])
    record={
          "id": id_counter,
          "name": name,
          "course": course,
          "marks": marks,
          "grade": grade
      }
    
    cohort1.append(record)
    # print(cohort1)
    print("Product added successfully!")
#---------------------------------------------------------------------------------------
def cohort():
    cohortText="""   SHOWCASING STUDENT INVENTORY 
"""
    print(cohortText)
    if len(cohort1) == 0:
        print("The list is empty ")
        return
    elif len(cohort1)== 1:
        viewOne(cohort1[0])
    else:
        viewMany(cohort1)
def viewOne(p):
    id, name, course, marks, grade =p.values()
    print(f'"Id"      :{id}\n"Name"    :{name}\n"Course"  :{course}\n"Marks"   :{marks}\n"Grade"   :{grade}\n')

def viewMany(p_list):
    print("-"*60)
    print(f"{"ID":^5}{"Name":<20}{"Course":<20}{"Marks":<10}{"Grade":^5}")
    print("-"*60)
    for p in p_list:
        id, name, course, marks, grade= p.values()
        print(f'{id:^5}{name:<20}{course:<20}{marks:<10}{grade:^5}')
    print("-"*60)

#---------------------------------------------------------------------------------------
def query():
    global cohort1
    text="""        1: Search by ID
        2: Search by Student Name / Course name
    """ 
    print(text)
    try:
        in2=int(input("Enter choice: "))
    except ValueError:
        print("Enter integer value")
        return
    if in2==1:
        searchId()
    elif in2==2:
        searchName()
    else:
        print("Enter valid choice")
        return
        
    def searchId():
        global cohort1
        try:
            sid=int(input("Enter the Student ID to search: "))
        except:
            print("Enter Integer Value")
        validId=[pid for pid in cohort1 if pid['id']==sid ]
        if len(validId)==0:
            print("No records found")
        else:
            viewOne(validId[0])

    def searchName():
        global cohort1
        sname=input("Enter the Student Name/Course Name to search: ").capitalize()
        if sname.strip() == "" or sname.strip() == "0":
            print("Entry is invalid")
            return
        else:
            validName=[pname for pname in cohort1 if pname['name'].lower()==sname.lower() or pname["course"].lower()==sname.lower()]
            if len(validName)==0:
                print("No records found")
            elif len(validName)==1:
                viewOne(validName[0])
            else:
                viewMany(validName)

#---------------------------------------------------------------------------------------
def revise():
    try:
        a=int(input("Enter the Stuent Id to update: "))

        updated= [pid for pid in cohort1 if pid['id']==a ]

        if len(updated)==0:
            print("ID not found")
        else:
            try:
                uname=str(input("Enter the new name of Student: ")).strip().title()
                if uname == "" or uname.isnumeric():
                    print("Name invalid")
                    return
                ucourse=str(input("Enter the new course: ")).strip().title()
                if ucourse == "" or ucourse.isnumeric():
                    print("Category Invalid")
                    return
                umarks=float(input("Enter the new marks: "))
                if umarks < 0.0 or umarks > 100.0:
                    print("umarks must be between 0.0 and 100.0 ")
                    return
                if umarks >= 85.0:
                    ugrade="A"
                elif 70.0 <= umarks < 85.0:
                    ugrade="B"
                elif 50.0 <= umarks < 70.0:
                    ugrade="C"
                else:
                    ugrade="F"
            except:
                print("Enter the valid value")
    except:
        print("Enter integer value")
    # updated[0]["id"]=a
    updated[0]['name']=uname
    updated[0]['course']=ucourse
    updated[0]['marks']=umarks
    updated[0]['grade']=ugrade
#---------------------------------------------------------------------------------------
def saves():
    try:
        with open("students.json","w") as file:
            json.dump(cohort1, file, indent=4)
        print("Data successfully saved")
    except IOError as e:
        print(f"There is error to save {e}")
#---------------------------------------------------------------------------------------
def loads():
    try:
        with open("students.json","r") as file:
            cohort1=json.load(file)    
        print("Data successfully loaded from students.json")
        
    except FileNotFoundError:
        print("No existing data file found. Starting with an empty cohort.")
        cohort1 = []
        id_counter = 0
    except json.JSONDecodeError:
        print("Error: students.json is corrupted. Starting with an empty cohort.")
        cohort1 = []
        id_counter = 0

#---------------------------------------------------------------------------------------
def main():
    while True:
       
        choice=menu()
        match choice:
            case 1:
                enroll()
            case 2:
                cohort()
            case 3:
                query()
            case 4:
                revise()
            case 5:
                try:
                    a=int(input("Enter the product Id to delete: "))
                except:
                    print("Enter integer value")
                    return
                updated= [pid for pid in cohort1 if pid['id']==a ]
                if len(updated) ==0:
                    print("ID not found")
                else:
                    viewOne(updated[0])
                    c1=input(f"Do you really want to delete product with id {a} (y/n)[No]: ").upper()
                    if c1 in['Y','YES']:
                        cohort1.remove(updated[0])
                        print("Succesfully Deleted")
                    else:
                        print("Deletion canceled")
            case 6:
                saves()
            case 7:
                loads()
            case 8:
                break
            case _:
                print("Invalid Choice. Try Again")
main()
                