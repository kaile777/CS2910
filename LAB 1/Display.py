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
            
            