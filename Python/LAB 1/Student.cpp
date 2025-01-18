#include <iostream>
#include <string>
#include "Student.h"

using namespace std;

int Student::numberOfStudents = 0;

Student::Student(string firstName, string lastName, int phoneNumber, string email)
: firstName(firstName), lastName(lastName), phoneNumber(phoneNumber), email(email)
{   
    id = numberOfStudents;
    numberOfStudents++;
}

int Student::getID() {
    return id;
}

string Student::getFirstName() {
    return firstName;
}

string Student::getLastName() {
    return lastName;
}

int Student::getPhoneNumber() {
    return phoneNumber;
}

string Student::getEmail() {
    return email;
}

void Student::getInfo() {
    cout << firstName << " " << lastName << endl;
    cout << id << endl;
    cout << phoneNumber << endl;
    cout << email << endl;
}



