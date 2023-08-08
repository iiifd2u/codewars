#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <typeinfo>


using namespace std;

float find_uniq(vector<float> v){
    vector<float> vec(v.size());
    copy(v.begin(), v.end(), vec.begin());
    const auto [min, max]  = minmax_element(begin(v), end(v)) ;
    // cout<<"min = "<<*min<<"\n";
    sort(vec.begin(), vec.end());
    vec.pop_back();
    vec.erase(vec.begin());
    if (vec[0]==*min){
        return *max;
    } else{
        return *min;
    }

}

int main()
{
    vector<float> n = {1, 1, 1, 1, 1, 5};
    cout << find_uniq(n) << "\n";
    return 0;
}