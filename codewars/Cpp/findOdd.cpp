#include <iostream>
#include <map>
#include <vector>

using namespace std;

int findOdd(vector<int> v){
    map<int, int> dict;
    for (int i = 0; i <= v.size(); i++)
    {
        if (!dict.count(v[i])){
            dict[v[i]]=1;
        } else{
            dict[v[i]]++;
        }
    }
    for (auto i{dict.begin()}; i!=dict.end(); i++)
    {
        cout << i->first << "="<<dict[i->first]<<"\n";
        if (dict[i->first]%2!=0){
            return i->first;
        }
    }
    return 0;
    
}

int main()
{
    cout << findOdd({ 2, 2, 2, 2, 3, 3, 5})<<"\n";
}