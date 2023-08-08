#include <iostream>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;

string duplicate_encoder(const string &str){
    map<char, int> dict_letters;
    string s;
    for (const char &el: str){
        if (el>='A'&& el<='Z'){
            s+=el+32;

        }else{
            s+=el;
        }
    }
    for (string::size_type i=0; i<s.size(); ++i){
        
        if (!dict_letters[s[i]]){
            dict_letters[s[i]]=1;
        } else{
            dict_letters[s[i]]+=1;
        }
    }
    string new_str;
    for (char const &c : s){
        // cout <<c<<":"<<dict_letters[c]<<"\n";
        if (dict_letters[c]>1){
            new_str+=")";
        }else{
            new_str+="(";
        }
    }
    return new_str;
}

int main()
{
    string str{"Success"};
    cout <<duplicate_encoder(str)<<"\n";
}