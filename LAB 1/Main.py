import Student as Student
import Course as Course
import FileProcessing as fp
import os
import Display
import Grade
import time

# os.system('cls')


def main():
    s_file = "students.csv"
    c_file = "courses.csv"
    g_file = "grades.csv"
    
    # auto interts lines into a list which will be parsed later
    raw_student_list = fp.getData(s_file)
    s_list = fp.parseStudentData(raw_student_list)

    # parses the csv and stores the strings in a list
    raw_courses_list = fp.getData(c_file)
    c_list = fp.parseCourseData(raw_courses_list)

    # parses the csv and stores the strings in a list
    raw_grades_list = fp.getData(g_file)
    fp.parseGradesData(raw_grades_list, c_list, s_list)
        
    title = """
    
    ********************
    *  School Database *
    ********************
    """

    main_menu = """
    
    Select an option:
    
    1. Print list of students
    2. Print list of courses
    3. Add Student
    4. Add Course
    5. Add Grade
    6. Update Student information
    7. Search Course
    8. Search Student
    100. Exit Program
    
    """
    stay_program = True
    
    
    while stay_program == True:
        print(title)
        print(main_menu)
        option = int(input("->  "))
        os.system('cls')
        
        if option == 1:
            
            display_students = """"
            
            Display Students:
            
            1. Display unsorted
            2. Display sorted by last name
            3. Exit
            
            """
            stay_1 = True
            while stay_1 == True:
                print(display_students)
                option = int(input("->  "))
                
                os.system('cls')
            
                if option == 1:
                    Display.display(s_list)
                elif option == 2:
                    Display.display(s_list, lambda student : student.lastName[0])
                elif option == 3:
                    stay_1 = False
                    os.system('cls')
                
        elif option == 2:
            display_courses = """
            
            Display Courses:
            
            1. Display unsorted
            2. Display sorted by course name
            3. Display by semester
            4. Display sorted by name and semester
            5. Exit
            
            """
            
            stay_2 = True
            
            while stay_2 == True:
                print(display_courses)
                option = int(input("->  "))
                
                os.system('cls')
                
                if option == 1:
                    Display.display(c_list)
                elif option == 2:
                    Display.display(c_list, lambda course : course.name[0])
                elif option == 3:
                    semester = input("Enter semester (fall or winter): ").upper()
                    Display.display(c_list, None, semester)
                elif option == 4:
                    semester = input("Enter semester (fall or winter): ").upper()
                    Display.display(c_list, lambda course : course.name[0], semester)
                elif option == 5:
                    stay_2 = False
                    os.system('cls')
            
        elif option == 3:
            stay_3 = True
            
            while stay_3 == True:
                os.system('cls')
                
                print("\nAdd Student:\n")
                firstName =    input("Enter first name   : ")
                lastName =     input("Enter last name    : ")
                phoneNum = int(input("Enter phone number : "))
                email =        input("Enter email        : ")
                s = Student.Student(firstName.upper(), lastName.upper(), phoneNum, email)
                s_list.append(s)
                option = input("Exit (Y/N): ").upper()
                if option == "Y":
                    stay_3 = False
                    os.system('cls')
                elif option == "N":
                    stay_3 = True
                else:
                    print("Incorrect input!")

                    
        elif option == 4:
            stay_4 = True
            
            while stay_4 == True:
                os.system('cls')
                
                print("Add Course:\n")
                name =     input("Enter name of course  : ")
                semester = input("Enter course semester : ")
                code =     input("Enter course code     : ")
                c = Course.Course(name, semester.upper(), code)
                c_list.append(c)
                print("\nCourse added:\n", course)
                option = input("Exit (Y/N): ").upper()
                if option == "Y":
                    os.system('cls')
                    stay_4 = False
                elif option == "N":
                    stay_4 = True
                else:
                    print("Incorrect input!")

        elif option == 5:
            
            os.system('cls')
            
            stay_5 = True
            
            while stay_5 == True:
            
                print("Add Student Grade:\n")
                lastName = input("Enter students last name: ").upper()
                courseCode = int(input("Enter course code: "))
                
                # check that student exists to be updated
                found = False
                inClass = False
                gradeAdded = False
                for student in s_list:
                    if student.lastName == lastName:
                        found = True
                        # check that student is registered in specified class
                        for grade in student.grades:
                            if grade.course.code == courseCode:
                                inClass = True
                        if inClass == False:
                            print("Student not in specified class!")
                        else:
                            grade_value = int(input("Enter grade (%): "))
                            for course in c_list:
                                if course.code == courseCode:
                                    c = course
                                    new_grade = Grade.Grade(c, grade_value)
                                    student.addGrade(new_grade)
                                    gradeAdded = True
                
                if gradeAdded == True:
                    print("Grade added successfuly!")
                elif found == False:
                    print("Student not found in system!")
                option = input("Exit (y/n): ").upper()
                
                if option == "Y":
                    os.system('cls')
                    stay_5 = False
                elif option == "Y":
                    stay_5 = True
                else:
                    print("Incorrect input!")
                    
                                
        elif option == 6:
            
            stay_6 = True
            
            while stay_6 == True:
                
                os.system('cls')
                
                print("Update Student Information:\n*** Back: Enter 0 ***\n")
                sID = int(input("Enter student ID: "))
                found = False
                s = None
                if sID == 0:
                    break
                for student in s_list:
                    if student.getStudentID() == sID:
                        found = True
                        s = student
                        break
                if found == False:
                    print("Student not found!")
                    option = input("Exit (Y/N): ").upper()
                    if option == "Y":
                        break
                else:
                    prompt = """
                    
                    Choose Which to Update:
                    1. First Name
                    2. Last Name
                    3. Phone Number
                    4. Email
                    
                    5. Back
                    
                    """
                    
                    keep_updating = True
                    
                    while keep_updating == True:
                        print(prompt, "\n")
                        option = int(input("->  "))
                        
                        if option == 1:
                            firstName = input("Enter First Name: ").upper()
                            s.updateFirstName(firstName)
                        elif option == 2:
                            lastName = input("Enter Last Name: ").upper()
                            s.updateLastName(lastName)
                        elif option == 3:
                            phoneNum = int(input("Enter Phone Number: "))
                            s.updatePhoneNumber(phoneNum)
                        elif option == 4:
                            email = input("Enter email: ")
                            s.updateEmail(email)
                        elif option == 5:
                            break
                        option = input("Continue updating this student? (Y/N) ").upper()
                        
                        if option == "Y":
                            keep_updating = True
                            os.system('cls')
                        elif option == "N":
                            keep_updating = False
                        else:
                            print("Invalid Input!")
                            
        elif option == 7:
            
            stay_7 = True
            
            while stay_7 == True:
                os.system('cls')
                prompt = """
                
                Search for Course
                
                1. Enter course code
                2. Enter course name
                3. Exit
                
                """
                print(prompt)
                
                option = int(input("->  "))
                
               
                found = False
                os.system('cls')
                if option == 1:
                    code = int(input("Enter Code: "))
                    element = code
                elif option == 2:
                    name = input("Enter Name: ").upper()
                    element = name
                elif option == 3:
                    break
                for course in c_list:
                    if option == 1:
                        if course.code == element:
                            found = True
                            course.getInfo()
                            break
                    elif option == 2:
                        if course.name == element:
                            found = True
                            course.getInfo()
                            break
                if found == False:
                    print("Course not found!")
                option = input("Exit (Y/N): ").upper()                
                if option == "Y":
                    stay_7 = False
                    os.system('cls')
                elif option == "N":
                    stay_7 = True
                else:
                    print("Invalid Input!")
                    
        elif option == 8:
            stay_8 = True
            
            while stay_8 == True:
                os.system('cls')
                prompt = """
                
                Search for Student
                
                1. Enter student last name
                2. Enter student phone number (last 4-digits)
                3. Exit
                
                """
                print(prompt)
                
                option = int(input("->  "))
                
                if option == 1:
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    stay_8 = False
                    os.system('cls')
                else:
                    print("Invalid Input!")
                
                
        elif option == 100:
            stay_program = False
        
        else:
            print("Invalid Input!")
        
        

main()


