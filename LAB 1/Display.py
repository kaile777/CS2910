from Student import Student
from Course import Course
import Sort


def display(list, f_comparator = None, semester = None):
    if len(list) == 0:
        return
    tmp_list = list.copy()
    
    if f_comparator != None:
        if isinstance(list[0], Student):
            tmp_list = Sort.merge_sort(tmp_list, lambda element : element.lastName[0])
        elif isinstance(list[0], Course):
            tmp_list = Sort.merge_sort(tmp_list, lambda element : element.name[0])
            
    if semester != None:
        for element in tmp_list:
            if element.semester == semester:
                print(element, "\n")
                
    else:
        for element in tmp_list:
            print(element, "\n")
            
            

def displayStudents(list, f_comparator = None):
    if len(list) == 0:
        return
    tmp_list = list.copy()
    
    if f_comparator != None:
        if isinstance(list[0], Student):
            tmp_list = Sort.merge_sort(tmp_list, lambda element : element.lastName[0])
        else:
            print("List content is not related to students!")
            return
            
    
    print(f"{'ID' : ^4}", end = " | ")
    print(f"{'LAST NAME' : ^13}", end = " | ")
    print(f"{'FIRST NAME' : ^15}", end = " | ")
    print(f"{'PHONE' : ^10}", end = " | ")
    print(f"EMAIL")
    for i in range(100):
        print("-", end = "")
    print()
    for student in tmp_list:
        print(f"{student.studentID : ^4}", end = " | ")
        print(f"{student.lastName : ^15}", end = ",")
        print(f"{student.firstName : ^15}", end = " | ")
        print(f"{student.phoneNum : ^10}", end=" | ")
        print(f"{student.email}")