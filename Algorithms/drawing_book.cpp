#include <bits/stdc++.h>

using namespace std;

int solve(int n, int p){
    // Complete this function
    int front_page = 1, back_page = n;
    int i;
    for (i = 0; i != n / 2; i++){
        
        if (front_page + 2 * i -1 <= p && p <= front_page + 2 * i)
            break;
        if (n % 2 == 0 && back_page - 2 * i <= p && p <= back_page - 2 * i + 1)
            break;
            
        if (n % 2 == 1 && back_page - 2 * i - 1 <= p && p <= back_page - 2 * i)    
            break;
        
        
        
    }
    return i;
         
}

int main() {
    int n;
    cin >> n;
    int p;
    cin >> p;
    int result = solve(n, p);
    cout << result << endl;
    return 0;
}

