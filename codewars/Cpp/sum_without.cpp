#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int sum_wo(vector<int> numbers){
    int sum = 0;
    if (numbers.size()<=1){
        return 0;
    }
    for (int i = 0; i!=numbers.size(); ++i){
        if (!numbers[i]){
            return 0;
        }
    }

    sort(numbers.begin(), numbers.end());
    for (int i = 1; i!=numbers.size()-1; ++i){
        sum+=numbers[i];
    }
    return sum;
}

int main()
{
    vector <int> nums = {3, 4, 0, 6, 3, 5, 9, 10};
    cout<<sum_wo(nums)<<"\n";
}