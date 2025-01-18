import Course as Course


class Grade:
    
    # course is a course object
    # grade is an integer number
    def __init__(self, course, grade):
        self.grade = grade
        self.course = course
    
    def getGrade(self):
        return self.grade
    
    def getInfo(self):
        print(f"{self.course}, {self.grade}%")
        
    def __str__(self):
        return f"{self.course}, {self.grade}%"