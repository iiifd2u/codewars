#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


vector<string> customSplit(const string &str, char separator){
    vector<string> strings;
    int start = 0, end =0;
    for(int i=0; i<=str.size(); i++){
        if(str[i]==separator||i == str.size()){
            end = i;
            string temp;
            temp.append(str, start, end-start);
            start =end+1;
            strings.push_back(temp);
        }
    }
    return strings;
}
string spinWords(const string &str){
    string new_str;
    vector<string> temp;
    for (string el:customSplit(str, ' ')){
        if (el.size()>=5){
            reverse(el.begin(), el.end());
        }
        temp.push_back(el);
    }
    for (int i=0; i!=temp.size()-1; ++i){
        new_str.append(temp[i]);
        new_str+=" ";
    }
    new_str.append(temp[temp.size()-1]);
    return new_str;
}

int main()
{

    cout<<spinWords("Hey fellow warriors")<<'\n';
    cout<<spinWords("a ab abc abcd abcde abcdef a ab")<<'\n';
    return 0;
}