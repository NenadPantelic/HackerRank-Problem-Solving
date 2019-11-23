#include <bits/stdc++.h>

using namespace std;

vector < int > getRecord(vector < int > s){
   
    int high_transitions = 0, low_transitions = 0;
    int current_max = s[0], current_min = s[0];
    for(int i = 0; i < s.size()-1; i++){
        
        if(s[i+1] > current_max){
            high_transitions++;
            current_max = s[i+1];
        }
        if (s[i+1] < current_min){
            low_transitions++;
            current_min = s[i+1];
        }
        
        
    }  
    
    vector<int> res = {high_transitions,low_transitions};
    return res;
    
}

int main() {
    int n;
    cin >> n;
    vector<int> s(n);
    for(int s_i = 0; s_i < n; s_i++){
       cin >> s[s_i];
    }
    vector < int > result = getRecord(s);
    string separator = "", delimiter = " ";
    for(auto val: result) {
        cout<<separator<<val;
        separator = delimiter;
    }
    cout<<endl;
    return 0;
}

