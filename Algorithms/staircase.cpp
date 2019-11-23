#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    string s = "";
    for(int i = 1; i <= n;i++){
        
        for (int j = n-i; j > 0;j--)
            cout << " ";
        s += "#";
        cout << s << endl;
    }
            
        
        
    return 0;
}

