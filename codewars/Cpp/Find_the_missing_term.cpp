#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

static long findMissing(const vector<long>& list){
    long summ_of_elems_pract = accumulate(list.begin(), list.end(), 0);
    cout <<summ_of_elems_pract<<"\n";
    long summ_of_elems_theor = (list.size()+1)*(list[0]+list[list.size()-1])/2;
    cout <<summ_of_elems_theor<<"\n";
    return summ_of_elems_theor-summ_of_elems_pract;

}

int main()
{
    vector <long> v = {1, 2, 3, 4, 5, 7};
    cout<<findMissing(v)<<"\n";
}