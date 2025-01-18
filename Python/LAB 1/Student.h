
#ifndef STUDENT_H
#define STUDENT_H

#include <string>

using namespace std;

class Student {

private:

    int id;
    string firstName;
    string lastName;
    int phoneNumber;
    string email;

    static int numberOfStudents;

public:

    Student(string firstName, string lastName, int phoneNumber, string email);

    int getID();
    string getFirstName();
    string getLastName();
    int getPhoneNumber();
    string getEmail();
    void getInfo();

};


#endif