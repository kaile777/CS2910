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
    
    1.  Print list of students
    2.  Print list of courses
    3.  Add Student
    4.  Add Course
    5.  Add Grade
    6.  Update Student information
    7.  Search Course
    8.  Search Student
    9.  Display Student Courses & Grades
    10. Display Student Average Total
    11. Display Student Average (Term)
    12. Display Course Average
    
    0. EXIT PROGRAM
    
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
                
                # write to students.csv file
                s_info_arr = [str(s.getStudentID()), s.getLastName(), s.getFirstName(), str(s.getPhoneNum()), s.getEmail()]
                fp.writeToFile(s_info_arr, s_file)
                
                
                # write to grades.csv file too
                # only adds ID, first name, and last name
                g_info_arr = [str(s.getStudentID()), s.getLastName(), s.getFirstName()]
                fp.writeToFile(g_info_arr, g_file)
                #
                # depending on total course number, append "na" to new student addition
                # specify student ID
                fp.appendToFileElements(g_file, s)
                
                
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
                name =     input("Enter name of course  : ").upper()
                semester = input("Enter course semester : ")

                # add course object to course list
                c = Course.Course(name, semester.upper())
                c_list.append(c)

                # add course to csv file
                c_info_arr = [c.getName(), c.getSemester(), str(c.getCode())]
                fp.writeToFile(c_info_arr, c_file)

                # append course to grades csv file
                # automatically "na" for students until grade is added
                fp.appendToFileElements(g_file)

                print("\nCourse added:\n", c)
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
                gradeAdded = False
                for student in s_list:
                    if student.lastName == lastName:
                        found = True
                        grade_value = int(input("Enter grade (%): "))
                        for course in c_list:
                            if course.code == courseCode:
                                new_grade = Grade.Grade(course, grade_value)
                                student.addGrade(new_grade)
                                course.addStudent(student)
                                fp.updateGrade(student, g_file, new_grade)
                                gradeAdded = True
                                break
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
                sID = int(input("Enter Student ID: "))
                found = False
                for student in s_list:
                    if student.studentID == sID:
                        Student.Student.updateStudent(student, s_file)
                        found = True
                        
                if found == False:
                    print("Student not found!")
                
                option = input("Exit? (Y/N) ").upper()
                if option == "N":
                    stay_6 = True
                    os.system('cls')
                elif option == "Y":
                    stay_6 = False
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
                
                1. Search by last name
                2. Search by phone number (last 4-digits)
                3. Exit
                
                """
                print(prompt)
                
                option = int(input("->  "))
                
                if option == 1:
                    lName = input("Enter Last Name: ").upper()
                    students_w_lastName = []
                    # check for multiple last names
                    for student in s_list:
                        if student.lastName == lName:
                            students_w_lastName.append(student)
                    if len(students_w_lastName) > 1:
                        print(f"Multiple students with last name: {lName}\n")
                        for student in students_w_lastName:
                            print(student, "\n")
                        sID = int(input("Please select student by ID: "))
                        match = False
                        for student in students_w_lastName:
                            if student.studentID == sID:
                                print(student)
                                match = True
                        if match == False:
                            print("Student ID entered does not match student list!")
                    elif len(students_w_lastName) == 1:
                        for student in students_w_lastName:
                            print(student)
                    else:
                        print(f"No students with last name, {lName}")
                elif option == 2:
                    number = input("Enter last 4 digits of student phone #: ")
                    match = False
                    for student in s_list:
                        last4digits = str(student.phoneNum)
                        last4digits = last4digits[-4:]
                        if last4digits == number[-4:]:
                            os.system('cls')
                            print(student,"\n")
                            match = True
                    if match == False:
                        number = number[-4:]
                        print(f"Student with phone # ending with: {number}, not found!")
                elif option == 3:
                    stay_8 = False
                    os.system('cls')
                else:
                    print("Invalid Input!")
                    
                option = input("Exit (Y/N): ").upper()                
                if option == "Y":
                    stay_8 = False
                    os.system('cls')
                elif option == "N":
                    stay_8 = True
        
        elif option == 9:
            stay_9 = True
            
            while stay_9 == True:
                os.system('cls')
                lName = input("Enter Student Last Name: ").upper()
                
                students_w_lastName = []
                # check for multiple last names
                for student in s_list:
                    if student.lastName == lName:
                        students_w_lastName.append(student)
                if len(students_w_lastName) > 1:
                    print(f"Multiple students with last name: {lName}\n")
                    for student in students_w_lastName:
                        print(student, "\n")
                    sID = int(input("Please select student by ID: "))
                    match = False
                    for student in students_w_lastName:
                        if student.studentID == sID:
                            # display student grades
                            for grade in student.grades:
                                grade.getInfo()
                                match = True
                    if match == False:
                        print("Student ID entered does not match student list!")
                elif len(students_w_lastName) == 1:
                    for student in students_w_lastName:
                        # display student grades
                            for grade in student.grades:
                                grade.getInfo()
                else:
                    print(f"No students with last name, {lName}")
                    
                option = input("Exit (Y/N): ").upper()                
                if option == "Y":
                    stay_9 = False
                    os.system('cls')
                elif option == "N":
                    stay_9 = True
        
        elif option == 10:
            stay_10 = True
            
            while stay_10 == True:
                os.system('cls')
                lName = input("Enter Student Last Name: ").upper()
                
                students_w_lastName = []
                # check for multiple last names
                for student in s_list:
                    if student.lastName == lName:
                        students_w_lastName.append(student)
                        
                courseCount = 0
                total = 0

                if len(students_w_lastName) > 1:
                    print(f"Multiple students with last name: {lName}\n")
                    for student in students_w_lastName:
                        print(student, "\n")
                    sID = int(input("Please select student by ID: "))
                    match = False
                    for student in students_w_lastName:
                        if student.studentID == sID:
                            # display student average
                            match = True
                            for grade in student.grades:
                                if grade.grade_val != "na":
                                    courseCount += 1
                                    total += int(grade.grade_val)
                            if courseCount > 0:
                                average = (total // courseCount) 
                                print(f"Total Average: {average}%")
                            
                    if match == False:
                        print("Student ID entered does not match student list!")
                elif len(students_w_lastName) == 1:
                    for student in students_w_lastName:
                        # display student average
                        total = 0
                        for grade in student.grades:
                            if grade.grade_val != "na":
                                    courseCount += 1
                                    total += int(grade.grade_val)
                        if courseCount > 0:
                            average = (total // courseCount) 
                            print(f"Total Average: {average}%")

                else:
                    print(f"No students with last name, {lName}")
                    
                option = input("Exit (Y/N): ").upper()                
                if option == "Y":
                    stay_10 = False
                    os.system('cls')
                elif option == "N":
                    stay_10 = True
            
        elif option == 11:
            stay_11 = True
            
            while stay_11 == True:
                os.system('cls')
                lName = input("Enter Student Last Name: ").upper()
                semester = input("Enter Term (Fall/Winter): ").upper()
                
                students_w_lastName = []
                # check for multiple last names
                for student in s_list:
                    if student.lastName == lName:
                        students_w_lastName.append(student)
                courseCount = 0
                total = 0
                if len(students_w_lastName) > 1:
                    print(f"Multiple students with last name: {lName}\n")
                    for student in students_w_lastName:
                        print(student, "\n")
                    sID = int(input("Please select student by ID: "))
                    match = False
                    for student in students_w_lastName:
                        if student.studentID == sID:
                            # display student average
                            match = True
                            for grade in student.grades:
                                if grade.grade_val != "na" and grade.course.semester == semester:
                                    courseCount += 1
                                    total += int(grade.grade_val)
                            if courseCount > 0:
                                average = (total // courseCount) 
                                print(f"Total Average: {average}%")
                            
                    if match == False:
                        print("Student ID entered does not match student list!")
                elif len(students_w_lastName) == 1:
                    for student in students_w_lastName:
                        # display student average
                        for grade in student.grades:
                            if grade.grade_val != "na" and grade.course.semester == semester:
                                    courseCount += 1
                                    total += int(grade.grade_val)
                        if courseCount > 0:
                            average = (total // courseCount) 
                            print(f"Total Average: {average}%")

                else:
                    print(f"No students with last name, {lName}")
                    
                option = input("Exit (Y/N): ").upper()                
                if option == "Y":
                    stay_11 = False
                    os.system('cls')
                elif option == "N":
                    stay_11 = True
                    
        elif option == 12:
            stay_12 = True
            
            while stay_12 == True:
                os.system('cls')
                print("Seach Course Average (%)\n")
                
                courseName = input("Enter Course Name: ").upper()
                
                match = False
                term_avg = 0
                for course in c_list:
                    if courseName == course.name:
                        match = True
                        # search and add student grades
                        count = 0
                        total = 0
                        for student in course.studentsInCourse:
                            for grade in student.grades:
                                if grade.course.name == courseName:
                                    total += int(grade.getGrade())
                                    count += 1
                                    
                        if count > 0:
                            term_avg = total // count
                            break

                if match == True:
                    print(f"Term Average for {courseName}: {term_avg}%")
                else:
                    print("Course has no grades associated with it!") 
                option = input("\nExit (Y/N): ").upper()                
                if option == "Y":
                    stay_10 = False
                    os.system('cls')
                elif option == "N":
                    stay_10 = True
                    
        elif option == -1:
            displayCourseStudents()
            
        elif option == 0:
            stay_program = False
        
        else:
            print("Invalid Input!")
        
        

main()


