#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int count_valleys(vector <char> ar, int n){
    
    int hike_point = 0;
    int i = 0;
    int count = 0;
    while(i < n){
        
        hike_point += (ar[i] == 'U') ? 1:-1;
        if (!hike_point && ar[i] == 'U' ) count++;
        i++;
        
        
    }
    return count;
    
    
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    vector<char> ar(n);
    
    for(int i = 0; i < n; i++)
        cin >> ar[i];
    
    int count = count_valleys(ar,n);
    cout << count << endl;
    
    
    return 0;
}

