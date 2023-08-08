#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<unsigned int> removeSmallest(const vector<unsigned int>& numbers){
    if (numbers.empty()){
        return numbers;
    }
    vector<unsigned int> nums(numbers.size());
    copy(numbers.begin(), numbers.end(), nums.begin());
    int m = *min_element(nums.begin(), nums.end());
    cout <<"m = "<< m << "\n";
    int f;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] == m){
            f = i;
            break;
        }
    }
    
    nums.erase(nums.begin()+f);
    return nums;
}

int main(){
    vector<unsigned int> nums = removeSmallest({2, 9, 2,4, 3, 0, 4});
    for (auto elem:nums){
        cout << elem<< "\t";
    }
    
}