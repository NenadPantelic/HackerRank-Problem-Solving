#include <bits/stdc++.h>

using namespace std;

vector < int > solve(vector < int > grades){
    int adder;
    for(int i = 0; i < grades.size(); i++){
        adder = 0;
        if (grades[i] >= 38){
            while ((grades[i] + adder) % 5 != 0)
                adder++;
            if (adder < 3)
                grades[i] += adder;
        }        
    }
    return grades;
}

int main() {
    int n;
    cin >> n;
    vector<int> grades(n);
    for(int grades_i = 0; grades_i < n; grades_i++){
       cin >> grades[grades_i];
    }
    vector < int > result = solve(grades);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? "\n" : "");
    }
    cout << endl;
    

    return 0;
}

