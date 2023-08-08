#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<vector<int>> vector_begin;
    for (int i=0;i<=vector_begin.size(); ++i){
        for (int j=0;j<=vector_begin[0].size(); ++j){
            cout<<vector_begin[i][j]<<"\t";
        }
        cout<<"\n";
    }
}