#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    //vector<int> arr(n);
    int val;
    int pos_count = 0, neg_count = 0, zero_count = 0;
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> val;
       if (val > 0) pos_count++;
       else if(val < 0) neg_count++;
       else zero_count++;
    }
    
    printf("%.6lf\n",double(pos_count)/n);
    printf("%.6lf\n",double(neg_count)/n);
    printf("%.6lf\n",double(zero_count)/n);

    return 0;
}

