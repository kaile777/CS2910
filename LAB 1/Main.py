from Student import Student
from Course import Course
import FileProcessing as fp
import os
import Display
from Grade import Grade

s_list = []
g_list = []
c_list = []











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
    11. Display Course Average

    0. EXIT PROGRAM
    
    """
    stay_program = True
    
    while stay_program == True:
        print(title)
        print(main_menu)
        
        while True:
            try:
                option = int(input("->  "))
                if option < 0 or option > 11:
                    raise Exception("Selection must be between 0 - 11!")
                break
            except:
                print("Select a numer!")
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
                
                while True:
                    try:
                        option = int(input("->  "))
                        if option < 1 or option > 3:
                            raise Exception("Selection must be between 1 - 3!")
                        break
                    except:
                        print("Invalid Input!")
                
                os.system('cls')
            
                if option == 1:
                    Display.displayStudents(s_list)
                elif option == 2:
                    Display.displayStudents(s_list, lambda student : student.lastName[0])
                elif option == 3:
                    stay_1 = False
                    os.system('cls')
                    break
                
                stay_1 = exit()
                
                
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
                
                while True:
                    try:
                        option = int(input("->  "))
                        if option < 1 or option > 5:
                            raise Exception("Selection must be between 1 - 5!")
                        break
                    except:
                        print("Invalid input!")
                
                os.system('cls')
                
                if option == 1:
                    Display.display(c_list)
                elif option == 2:
                    Display.display(c_list, lambda course : course.name[0])
                elif option == 3:
                    
                    while True:
                        try:    
                            semester = input("Enter semester (fall or winter): ").upper()
                            if semester != "FALL" and semester != "WINTER":
                                raise Exception()
                            break
                        except:
                            print("Invalid Input!")
                            
                    Display.display(c_list, None, semester)
                elif option == 4:
                    
                    while True:
                        try:    
                            semester = input("Enter semester (fall or winter): ").upper()
                            if semester != "FALL" and semester != "WINTER":
                                raise Exception()
                            break
                        except:
                            print("Invalid Input!")
                    
                    Display.display(c_list, lambda course : course.name[0], semester)
                elif option == 5:
                    stay_2 = False
                    os.system('cls')
                    break
                    
            
                stay_2 = exit()
            
        elif option == 3:
            stay_3 = True
            
            while stay_3 == True:
                os.system('cls')
                
                print("\nAdd Student:\n")
                firstName =    input("Enter first name   : ")
                lastName =     input("Enter last name    : ")
                
                # check phone number input validity
                while True:
                    try:
                        phoneNum = int(input("Enter phone number : "))
                        digits = getDigits(phoneNum)
                        if digits > 0 and digits <= 10:
                            break
                        print("Invalid Phone Number!")
                        print("Greater than 0 | Less than or equal to 10")
                    except:
                        print("Must be a number!")
                        
                email =        input("Enter email        : ")
                s = Student(firstName.upper(), lastName.upper(), phoneNum, email)
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
                
                
                stay_3 = exit()


        elif option == 4:
            stay_4 = True

            while stay_4 == True:
                os.system('cls')

                print("Add Course:\n")
                
                name =     input("Enter name of course                   : ").upper()

                while True:
                    try:
                        semester = input("Enter course semester (Fall or Winter) : ").upper()
                        if semester != "FALL" and semester != "WINTER":
                            raise Exception("Selection must be FALL or WINTER!")
                        
                        c = Course(name, semester)
                        dup_course = dupCourse(c, c_list)
                
                        if dup_course == True:
                            print(f"{c.name}, {c.semester} already exists!")
                            raise Exception()
                        break
                    except:
                        print("Invalid Input")
                        
                
                    
                
                # add course object to course list
                c_list.append(c)

                # add course to csv file
                c_info_arr = [c.getName(), c.getSemester(), str(c.getCode())]
                fp.writeToFile(c_info_arr, c_file)

                # append course to grades csv file
                # automatically "na" for students until grade is added
                fp.appendToFileElements(g_file)

                print("\nCourse added:\n", c)
                
                stay_4 = exit()

        elif option == 5:

            os.system('cls')

            stay_5 = True
            
            print("Add Student Grade:\n")
            
            while stay_5 == True:
                
                lastName = input("Enter students last name: ").upper()
                sID = inputLastName(lastName, s_list)
                student = s_list[sID - 1]
                
                while True:
                    try:
                        courseCode = int(input("Enter course code: "))
                        c_exists = courseExists(c_list[courseCode - 1], c_list)
                        if not c_exists:
                            raise Exception(f"{courseCode} does not exists!")
                        break 
                    except:
                        print("Invalid Input!\n")
                        for course in c_list:
                            print(f"{course.code}  {course.name}")         
                    
                while True:
                    try:
                        grade_value = int(input("Enter grade (0-100)% : "))
                        if grade_value < 0 or grade_value > 100:
                            raise Exception("Grade value must be >= 0 AND <= 100!")
                        break
                    except:
                        print("Invalid Input!")
                        
                        
                new_grade = Grade(c_list[courseCode - 1], grade_value)
                student.addGrade(new_grade)
                c_list[courseCode - 1].addStudent(student)
                fp.updateGrade(student, g_file, new_grade)
                gradeAdded = True
                        
                if gradeAdded == True:
                    print("Grade added successfuly!")
                
                stay_5 = exit()
                    
                                
        elif option == 6:
            
            stay_6 = True
            
            while stay_6 == True:
                
                os.system('cls')
                print("Update Student Information:\n")
                
                while True:
                    try:
                        sID = int(input("Enter Student ID: "))
                        break
                    except:
                        print("Invalid Input!")
                
                found = False
                for student in s_list:
                    if student.studentID == sID:
                        Student.updateStudent(student, s_file)
                        found = True
                        
                if found == False:
                    print("Student not found!")
                
                stay_6 = exit()
                
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
                
                while True:
                    try:
                        option = int(input("->  "))
                        if option < 1 or option > 3:
                            raise Exception("Selection must be between 1 - 3!")
                        break
                    except:
                        print("Invalid Input!")
               
                found = False
                os.system('cls')
                
                code = None
                
                if option == 1:
                    while True:
                        try:
                            code = int(input("Enter Code: "))
                            for course in c_list:
                                if course.code == code:
                                    found = True
                            if found == False:
                                raise Exception("Invalid Code!")
                            break
                        except:
                            print("Invalid Code")
                        
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
                        
                # reduntant
                if found == False:
                    print("Course not found!")
                    
                stay_7 = exit()
                    
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
                
                while True:
                    try:
                        option = int(input("->  "))
                        if option < 1 or option > 3:
                            raise Exception()
                        break
                    except:
                        print("Inavlid Input!")
                
                if option == 1:
                    lastName = input("Enter Last Name: ")
                    sID = inputLastName(lastName, s_list)
                    student = s_list[sID - 1]
                    print(student)
                elif option == 2:
                    
                    while True:
                        try:
                            number = int(input("Enter last 4 digits of student phone #: "))
                            if getDigits(number) > 4:
                                print("Must be 4 digits!")
                                raise Exception()
                            break
                        except:
                            print("Invalid Input!")
                            
                    match = False
                    for student in s_list:
                        last4digits = student.phoneNum
                        last4digits = last4digits[-4:]
                        if last4digits == number[-4:]:
                            os.system('cls')
                            print("\n",student,"\n")
                            match = True
                    if match == False:
                        number = number[-4:]
                        print(f"Student with phone # ending with: {number}, not found!")
                elif option == 3:
                    stay_8 = False
                    os.system('cls')
                else:
                    print("Invalid Input!")
                    
                stay_8 = exit()
        
        elif option == 9:
            stay_9 = True
            
            while stay_9 == True:
                os.system('cls')
                print("Display Student Courses & Grades\n")
                
                lastName = input("Enter Last Name: ")
                sID = inputLastName(lastName, s_list)
                student = s_list[sID - 1]
                
                for grade in student.grades:
                    print(grade)
                    
                stay_9 = exit()
        
        elif option == 10:
            stay_10 = True
            
            while stay_10 == True:
                os.system('cls')
                print("View Student Averages\n")
                
                lastName = input("Enter Student Last Name: ").upper()
                sID = inputLastName(lastName, s_list)
                student = s_list[sID - 1]
                
                prompt = """
                
                1. Display total average
                2. Display semester average
                3. Exit
                
                """
                
                print(prompt)
                while True:
                    try:
                        option = int(input("->  "))
                        if option < 4 and option > 0:
                            break
                        raise Exception("Invalid Input!")
                    except:
                        print("Please try again...\n")
                        
                total = 0
                courseCount = 0
                sem = ""
                
                if option == 1:
                    # display student average
                    for grade in student.grades:
                        if grade.grade_val != "na":
                            courseCount += 1
                            total += int(grade.grade_val)
                elif option == 2:
                    # display term average
                    
                    while True:
                        try:
                            sem = input("Enter Semester: ").upper()
                            if sem != "FALL" or sem != "WINTER":
                                raise Exception()
                            break
                        except:
                            print("Invalid Input")

                    for grade in student.grades:
                        if grade.grade_val != "na" and grade.course.semester == sem:
                            courseCount += 1
                            total += int(grade.grade_val)
                elif option == 3:
                    break
                    
                if courseCount > 0:
                    average = (total // courseCount) 
                    print(f"Total Average: {average}%")
                else:
                    print(f"No courses taken in {sem}!")
                    
                stay_10 = exit()
   
   

                    
        elif option == 11:
            stay_11 = True
            
            while stay_11 == True:
                os.system('cls')
                print("Seach Course Average (%)\n")
                
                found = False
                while True:
                    try:
                        courseName = input("Enter Course Name: ").upper()
                        for course in c_list:
                            if courseName == course.name.upper():
                                found = True
                                break
                        if found == False:
                            raise Exception()
                        break
                    except:
                        print("Invalid Input!")
                        
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
                                    break
                                    
                        if count > 0:
                            term_avg = total // count
                            break

                if match == True:
                    print(f"Term Average for {courseName}: {term_avg}%")
                else:
                    print("Course has no grades associated with it!") 
                
                stay_11 = exit()

            
        elif option == 0:
            stay_program = False
        
        else:
            print("Invalid Input!")
        

        
        
        
def dupCourse(course, c_list):
    for c in c_list:
        if c.code == course.code:
            return True
    return False
            


# HELPER FUNCTIONS
def getDigits(num):
    digits = 0
    while num != 0:
        digits += 1
        num = num // 10
    return digits


def inputLastName(lastName, s_list):
    lastName = lastName.upper()
    unique_list = uniqueLastName(lastName, s_list)
    sID = 0
    if len(unique_list) > 1:
        print("Duplicate last names found!\n")
        for student in unique_list:
            print(f"{student.studentID}  {student.lastName}, {student.firstName}")
        while True:
            sID = int(input("Please Enter Student ID: "))
            for student in unique_list:
                if sID == student.studentID:
                    return sID
            print("Student not found!")
    elif len(unique_list) < 1:
        print(f"({lastName}) not found!")
        while True:
            lastName = input("Enter Last Name: ").upper()
            unique_list = uniqueLastName(lastName, s_list)
            if len(unique_list) == 1:
                break
            print("DUPLICATE\n")
            for student in unique_list:
                print(f"{student.studentID}  {student.lastName}, {student.firstName}")
            sID = int(input("Please Enter Student ID: "))
            for student in unique_list:
                if sID == student.studentID:
                    return sID
        
    return unique_list[0].studentID


def uniqueLastName(lName, s_list):
    students_w_lastName = []
    # check for multiple last names
    for student in s_list:
        if student.lastName == lName:
            students_w_lastName.append(student)
    return students_w_lastName
        

def courseExists(course, c_list):
    for c in c_list:
        if c.code == course.code:
            return True
        if c.name == course.name and c.semester == course.semester:
            return True
    return False


def showCourseContents(c_list):
    for course in c_list:
        print(f"{course.name}\n**********\n")
        for student in course.studentsInCourse:
            print(student, "\n")


def exit():
    while True:
        try:
            option = input("Exit (Y/N): ").upper()
            if option != "Y" and option != "N":
                raise Exception("Selection must be (Y) or (N)!")
            break
        except:
            print("Invalid Input!")
                
    if option == "Y":
        os.system('cls')
        return False

    return True

            
        
        

main()


