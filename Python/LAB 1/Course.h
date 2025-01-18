
#ifndef COURSE_H
#define COURSE_h

#include <string>

using namespace std;

class Course {

private:
    string name;
    int code;
    string semester;

    static int numberOfCourses;

public:
    Course(string name, string semester);

    string getName();
    int getCode();
    string getSemester() ;

    string getInfo();


};




#endif