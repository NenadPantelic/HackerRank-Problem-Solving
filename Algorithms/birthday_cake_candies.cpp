#include <bits/stdc++.h>

using namespace std;

int birthdayCakeCandles(int n, vector <int> ar) {
    sort(ar.begin(),ar.end());
    
    int max = ar[n-1];
    int count = 0;
    for(int i = n-1; i >= 0;i--){
        if (ar[i] == max) count++;
        else break;
    }
    
    return count;
}

int main() {
    int n;
    cin >> n;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = birthdayCakeCandles(n, ar);
    cout << result << endl;
    return 0;
}

