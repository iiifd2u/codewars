#include <iostream>
#include <cstdlib>

using namespace std;

int paperwork(int n, int m){
    if (n<0 or m<0){
        return 0; 
    };
    return n*m;
}

int main()
{
    cout<<paperwork(5, 5)<<"\n";
    cout<<paperwork(-5, 5)<<"\n";
    cout<<paperwork(5, -5)<<"\n";
}