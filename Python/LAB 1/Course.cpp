#include <string>
#include <iostream>
#include "Course.h"

using namespace std;

int Course::numberOfCourses = 0;

Course::Course(string name, string semester)
: name(name), semester(semester)
{
    numberOfCourses++;
    code = numberOfCourses;
}

string Course::getName() {
    return name;
}

int Course::getCode() {
    return code;
}

string Course::getSemester() {
    return semester;
}

string Course::getInfo() {
    string info = name + " " + semester + to_string(code) ;
    return info;
}

