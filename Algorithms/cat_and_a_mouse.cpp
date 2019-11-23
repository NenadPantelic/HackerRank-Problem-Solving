#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

string mouse(int x,int y, int z){
    
    string cat;
    if (abs(x-z) == abs(y-z)) cat = "Mouse C";
    else cat = (abs(x-z) < abs(y-z))? "Cat A": "Cat B";
    return cat;
    
    
}

int main(){
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        int x;
        int y;
        int z;
        cin >> x >> y >> z;
        cout << mouse(x,y,z) << endl;
        
    }
    return 0;
}
    
