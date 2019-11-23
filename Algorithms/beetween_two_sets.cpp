#include <bits/stdc++.h>

using namespace std;

int getTotalX(vector <int> a, vector <int> b) {
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    int max_a = a[a.size()-1];
    int min_b = b[0];
    int flag_a,flag_b, count  = 0;
    for(int factor = max_a; factor <= min_b; factor++){
        flag_a = 1;
        flag_b = 1;
        for(int i = 0; i < a.size(); i++)
            if (factor % a[i] != 0){
                
                flag_a = 0;
                break;
            }
        for (int j = 0; j < b.size(); j++)
            if (b[j] % factor != 0){
                
                flag_b = 0;
                break;
            }
        
        if (flag_a && flag_b)
            count++;
                    
 
        
    }
    return count;
}

int main() {
    int n;
    int m;
    cin >> n >> m;
    vector<int> a(n);
    for(int a_i = 0; a_i < n; a_i++){
       cin >> a[a_i];
    }
    vector<int> b(m);
    for(int b_i = 0; b_i < m; b_i++){
       cin >> b[b_i];
    }
    
    int total = getTotalX(a, b);
    cout << total << endl;
    return 0;
}

