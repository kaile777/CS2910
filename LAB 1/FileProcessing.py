import Student
import Course
import Grade
import csv

# TODO: refactor imports across all files

# Reads data from CSV file
# Each line is stored in a list
# Updates student objects member grades list
def getData(file_name):
    file = open(file_name, "r")
    list = file.readlines()
    file.close()
    return list


def parseGradesData(raw_list, course_list, student_list):
    # create 2d array of empty strings
    string_test = raw_list[0].split(";")
    cols = len(string_test)
    rows = len(raw_list)
    arr = []
    for _ in range(rows):
        arr.append([""] * cols)
    
    
        
    # outer loop that iterates over each line of raw string
    for i in range(0, len(raw_list)):        
        # inner loop that iterates over each char of the line
        raw_list[i] = raw_list[i].strip("\n")
        arr[i] = raw_list[i].split(";")
        
        
    sID_index = 0
    grade_index = 3
    
    # find student with matching student ID
    # create grade object
    student_index = 0 
    for student in student_list:

        if student.studentID == int(arr[student_index][sID_index]):
            # reset course ID to 1 for each new student iteration
            course_id = 1
            # once student is found, go through grades in arr[]
            # and extract the course, then create a grade object
            # using the course and grade_val
            # append this grade to student.grades array[]
            
            for grade_val in arr[student_index][grade_index:]:
                if grade_val == "na":
                    course_id += 1
                elif grade_val != "na":
                    # get int(grade_val)
                    value = int(grade_val)
                    _course = course_list[course_id - 1]
                    _grade = Grade.Grade(_course, value)
                    student.grades.append(_grade)
                    _course.addStudent(student)
                    course_id += 1
            
        student_index += 1
        
        
        
        
        
        

# takes in course.csv file and parses information
# returns list of course objects
def parseCourseData(raw_list):
    course_list = []
    for i in range(0, len(raw_list)):
        raw_list[i] = raw_list[i].strip("\n")
        c_list = raw_list[i].split(";")
        course = Course.Course(c_list[0].upper(), c_list[1].upper())
        course_list.append(course)
    return course_list

# takes in student.csv file and parses information
# returns list of student objects
def parseStudentData(raw_list):
    student_list = []
    for i in range(0, len(raw_list)):
        raw_list[i] = raw_list[i].strip("\n")
        s_list = raw_list[i].split(";")
        student = Student.Student(s_list[2].upper(), s_list[1].upper(), int(s_list[3]), s_list[4])
        student_list.append(student)
    return student_list

# takes in array of elements to add for grades, students, or courses
# converts elements into csv format, adding them to appropriate csv file
def writeToFile(element_add, csv_file):
    # open the csv file in append mode
    # delimiter = ";"
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(element_add)
        

# appends "na" to grades file when a new course is added
def appendToFileElements(csv_file, student = None, grade = None):
    # data to append to each row
    data_to_add = "na"

    # read the current csv file
    rows = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if student == None:
                # append the data_to_add to end of each row
                row.append(data_to_add)
                rows.append(row)
            # when student ID has a value, it means we are 
            # appending "na" to a NEW student only
            else:
                student_id_index = 0
                if int(row[student_id_index]) == student.getStudentID():
                    # append the data_to_add to end of each row
                    if grade == None:
                        for i in range(0, int(Course.Course.numberOfCourses)):
                            row.append(data_to_add)
                    else:
                        # 2: index 1 before grade values are stored
                        # course codes start at 1
                        row[2 + grade.course.code] = grade.grade_val
                rows.append(row)
                    
            
    # write updated rows back into csv file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(rows)
        

# take in student ID
# scan grades.csv until student ID found
# starting at 3rd index, scan until courseID matches index
# replace "na" with integer grade_value

def updateGrade(student, g_file, grade):
    arr = [str(student.studentID), student.lastName, student.firstName]
    appendToFileElements(g_file, student, grade)


def udpateIndex(csv_file, index, add_element, sID):
    rows = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if int(row[0]) == sID:
                row[index] = add_element
            rows.append(row)
    
    # write updated rows back into csv file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(rows)