#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> nums)
{
    int firstLen = nums.size();
    int answer = 0;
    
    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());
    int secondLen = nums.size();
    
    int half = firstLen / 2;
    cout << half << endl;
    cout << secondLen << endl;
    
    if(half < secondLen) {
        answer = half;
    } else {
        answer = secondLen;
    }
    
    
    return answer;
}