#include <iostream>
#include <set>
#include <numeric>

using namespace std;

int solution(int number){
    set<int> delimers;
    for (int i=0; i<number; i+=3){
        delimers.insert(i);
    }
    for (int i=0; i<number; i+=5){
        delimers.insert(i);
    }
    int sum = accumulate(delimers.begin(), delimers.end(), 0);
    return sum;
}

int main()
{
    // cout<<"lol";
    cout<<solution(1000)<<'\n';
    return 0;
}