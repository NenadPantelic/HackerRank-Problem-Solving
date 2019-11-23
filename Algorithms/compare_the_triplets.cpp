#include <bits/stdc++.h>

using namespace std;

vector < int > solve(int a0, int a1, int a2, int b0, int b1, int b2){
    // Complete this function
    int a[3] = {a0,a1,a2};
    int b[3] = {b0,b1,b2};
    int res1 = 0,res2 = 0;
    for(int i = 0; i<3;i++){
        
        res1 += (a[i] > b[i])? 1:0;
        res2 += (a[i] < b[i])? 1:0;
        
        
    }

    vector <int> sol = {res1,res2};
    return sol;
}

int main() {
    int a0;
    int a1;
    int a2;
    cin >> a0 >> a1 >> a2;
    int b0;
    int b1;
    int b2;
    cin >> b0 >> b1 >> b2;
    vector < int > result = solve(a0, a1, a2, b0, b1, b2);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? " " : "");
    }
    cout << endl;
    

    return 0;
}

