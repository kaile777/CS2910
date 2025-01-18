class Course:
    
    def __init__(self, name, semester, code):
        self.name = name
        self.semester = semester
        self.code = code
        
        self.studentsInCourse = []
        
    def __str__(self):
        return f"{self.name}, {self.semester}, {self.code}"
        
    def getName(self):
        return self.name

    def getSemester(self):
        return self.semester
    
    def getCode(self):
        return self.code
    
    def getInfo(self):
        print(f"Name: {self.name}\nSemester: {self.semester}\nCode: {self.code}")
        
    def addStudent(self, student):
        self.studentsInCourse.append(student)