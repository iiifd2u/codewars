#include <vector>
#include<algorithm>
#include <iostream>

using namespace std;

size_t findSmallest(const vector<int>& v)
{
   return *min_element(v.begin(), v.end());
}

int main(){
    cout << findSmallest({1, 2,3})<<"\n";
}