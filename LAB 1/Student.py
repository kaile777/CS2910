import Grade as Grade
import Course as Course


class Student:
    
    __numberOfStudents = 0
    
    def __init__(self, firstName, lastName, phoneNum, email):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNum = phoneNum
        self.email = email
        
        Student.__numberOfStudents += 1
        self.studentID = Student.__numberOfStudents
        
        # initially all NA
        # must hold grade objects
        # once grades.csv is parsed, grades[] will be updated
        self.grades = []
        
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
        return self.studentID

    def addGrade(self, grade):
        self.grades.append(grade)
        
    def displayGrades(self):
        for grade in self.grades:
            print(grade)
        
    def updateFirstName(self, new_name):
        self.firstName = new_name
        
    def updateLastName(self, new_name):
        self.lastName = new_name
        
    def updatePhoneNumber(self, new_number):
        self.phoneNum = new_number
    
    def updateEmail(self, new_email):
        self.email = new_email
        
    
        

