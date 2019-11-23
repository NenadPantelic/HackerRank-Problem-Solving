#include <bits/stdc++.h>

using namespace std;

string timeConversion(string s) {
    string hour = s.substr(0,2);
    string time = s.substr(s.length()-2,2);
    string rest = s.substr(2,6);
    string new_time;
    if (time == "AM"){
        if (hour == "12") new_time = "00" + rest;
        else new_time = hour + rest;
        
    }
    
    else {
        
        if (hour == "12") new_time = "12" + rest;
        else
            new_time = to_string(stoi(hour) + 12) + rest; 
        
    }
    return new_time;
}

int main() {
    string s;
    cin >> s;
    string result = timeConversion(s);
    cout << result << endl;
    return 0;
}

