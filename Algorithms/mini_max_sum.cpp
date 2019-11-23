#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> arr(5);
    for(int arr_i = 0; arr_i < 5; arr_i++){
       cin >> arr[arr_i];
    }
    sort(arr.begin(), arr.end());
    long suma = 0;
    for(int element:arr)
        suma += element;
    cout << suma - arr[4] << " " << suma - arr[0] << endl;
    return 0;
}

