from Course import Course
import FileProcessing as fp
import os



   
class Student:
    
    __numberOfStudents = 0
    
    def __init__(self, firstName, lastName, phoneNum, email):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNum = int(phoneNum)
        self.email = email
        
        Student.__numberOfStudents += 1
        self.studentID = Student.__numberOfStudents
        
        # initially all NA
        # must hold grade objects
        # once grades.csv is parsed, grades[] will be updated
        self.grades = []

        for i in range(0, Course.numberOfCourses):
            self.grades.append("na")
        
    def __str__(self):
        return f"{self.firstName} {self.lastName}\nID: {self.studentID}\n{self.phoneNum}\n{self.email}"
        
    def getInfo(self):
        print(f"{self.firstName} {self.lastName}\nID: {self.studentID}\n{self.phoneNum}\n{self.email}")
        
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getPhoneNum(self):
        return self.phoneNum

    def getEmail(self):
        return self.email
    
    def getStudentID(self):
        return int(self.studentID)

    def addGrade(self, grade):
        self.grades.append(grade)
        
    def displayGrades(self):
        for grade in self.grades:
            print(grade)
        
    def updateStudent(student, s_file):
        
        prompt = """
                    
        Choose Which to Update:
        1. First Name
        2. Last Name
        3. Phone Number
        4. Email
        
        0. Back
        
        """
        
        keep_updating = True
                    
        while keep_updating == True:
            print(prompt, "\n")
            option = int(input("->  "))
            
            pos_lName = 1
            pos_fName = 2
            pos_phone = 3
            pos_email = 4

            
            if option == 1:
                firstName = input("Enter First Name: ").upper()
                student.firstName = firstName
                fp.udpateIndex(s_file, pos_fName, firstName, student.studentID)
            elif option == 2:
                lastName = input("Enter Last Name: ").upper()
                student.lastName = lastName
                fp.udpateIndex(s_file, pos_lName, lastName, student.studentID)
            elif option == 3:
                phoneNum = int(input("Enter Phone Number: "))
                student.phoneNum = phoneNum
                fp.udpateIndex(s_file, pos_phone, phoneNum, student.studentID)
            elif option == 4:
                email = input("Enter email: ")
                student.email = email
                fp.udpateIndex(s_file, pos_email, email, student.studentID)
            elif option == 0:
                return
            option = input("Continue updating this student? (Y/N) ").upper()
            
            if option == "Y":
                keep_updating = True
                os.system('cls')
            elif option == "N":
                keep_updating = False
            else:
                print("Invalid Input!")



