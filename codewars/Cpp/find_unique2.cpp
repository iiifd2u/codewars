#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>


using namespace std;

float find_uniq(const vector<float> &v){
    unordered_set<float> uos(v.begin(), v.end());
    multiset<float> s(v.begin(), v.end());
    vector<float> diff(s.size());
    vector <float> result(1); 
    set_difference(s.begin(), s.end(),
    uos.begin(), uos.end(),diff.begin());
    set_difference(uos.begin(), uos.end(),
    diff.begin(), diff.end(),result.begin());
    return *begin(result);
}

int main()
{
    vector<float> n = {1, 1, 1, 1, 1, 1};
    cout << find_uniq(n) << "\n";
    return 0;
}