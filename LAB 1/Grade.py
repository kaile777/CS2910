import Course as Course


class Grade:
    
    # course is a course object
    # grade is an integer number
    def __init__(self, course, grade_val):
        self.grade_val = grade_val
        self.course = course
    
    def getGrade(self):
        return self.grade_val
    
    def getInfo(self):
        print(f"{self.course}, {self.grade_val}%")
        
    def __str__(self):
        return f"{self.course}, {self.grade_val}%"