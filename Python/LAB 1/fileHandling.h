#ifndef FILEHANDLING_H
#define FILEHANDLING_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
using row = vector<string>;
using db = vector<row>;

vector<string> split(string text, char delim) {
    string line;
    vector<string> vec;
    stringstream ss(text);
    while(getline(ss, line, delim)) {
        vec.push_back(line);
    }
    return vec;
}

void readFromFile(db & Data, string fileName)
{
  ifstream file(fileName);
  string line, delim = ";";
    
  if (!file.is_open()) {
    cout << "File not opened...\n";
  }
  else {
    while(file) {
        file >> line;
        if (!line.empty()) {
          row r =split(line, ';');
          Data.push_back(r);
          line.clear();
        }
    }

  }
  
  file.close();
  
}






#endif