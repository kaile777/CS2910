import Student as Student
import Course as Course
import Grade as Grade

# Reads data from CSV file
# Each line is stored in a list
# Updates student objects member grades list
def getData(file_name):
    file = open(file_name, "r")
    list = file.readlines()
    file.close()
    return list


def parseGradesData(raw_list, course_list, student_list):
    grade_list = []
    
    # outer loop that iterates over each line of raw string
    for i in range(0, len(raw_list)):
        sID = 0
        fName = ""
        lName = ""
        course1_grade = None
        course2_grade = None
        course3_grade = None
        course4_grade = None
        segment = 0
        element = ""
        # inner loop that iterates over each char of the line
        for j in range(0, len(raw_list[i])):
            if raw_list[i][j] == "\n":
                course4_grade = element
                break
            if raw_list[i][j] != ";":
                element += raw_list[i][j]
            if raw_list[i][j] == ";":
                if segment == 0:
                    sID = element
                elif segment == 1:
                    lName = element
                elif segment == 2:
                    fName = element
                elif segment == 3:
                    course1_grade = element
                elif segment == 4:
                    course2_grade = element
                elif segment == 5:
                    course3_grade = element
                element = ""
                segment += 1
                
        
        
        if int(sID) == student_list[i].getStudentID():
            if course1_grade != "na":
                student_list[i].addGrade(Grade.Grade(course_list[0], int(course1_grade)))
            if course2_grade != "na":
                student_list[i].addGrade(Grade.Grade(course_list[1], int(course2_grade)))
            if course3_grade != "na":
                student_list[i].addGrade(Grade.Grade(course_list[2], int(course3_grade)))
            if course4_grade != "na":
                student_list[i].addGrade(Grade.Grade(course_list[3], int(course4_grade)))

            
        


# takes in course.csv file and parses information
# returns list of course objects
def parseCourseData(raw_list):
    course_list = []
    
    # outer loop that iterates over each line of raw string
    for i in range(0, len(raw_list)):
        name = ""
        semester = ""
        code = 0
        segment = 0
        element = ""
        # inner loop that iterates over each character of the line
        for j in range(0, len(raw_list[i])):
            if raw_list[i][j] == "\n":
                code = element
                break
            if raw_list[i][j] != ";":
                element += raw_list[i][j]
            if raw_list[i][j] == ";":
                if segment == 0:
                    name = element
                elif segment == 1:
                    semester = element
                element = ""
                segment += 1
                
        course = Course.Course(name, semester.upper(), int(code))
        course_list.append(course)
        
    return course_list


# takes in student.csv file and parses information
# returns list of student objects
def parseStudentData(raw_list):
    student_list = []
    # outer loop that iterates over each line of raw string
    for i in range(0, len(raw_list)):
        id = 0
        fName = ""
        lName = ""
        phoneNum = 0
        email = ""
        element = ""
        segment = 0
        # inner loop that iterates over each character of the line
        for j in range(0, len(raw_list[i])):
            if raw_list[i][j] == "\n":
                email = element
                break
            if raw_list[i][j] != ";":
                element += raw_list[i][j]
            if raw_list[i][j] == ";":
                if segment == 0:
                    id = int(element)
                elif segment == 1:
                    lName = element
                elif segment == 2:
                    fName = element
                elif segment == 3:
                    phoneNum = int(element)
                element = ""
                segment += 1
        
        student = Student.Student(fName.upper(), lName.upper(), phoneNum, email)
        student_list.append(student)
        
    return student_list

