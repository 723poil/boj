#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    int before_element = -1;
    
    vector<int>::iterator itor = arr.begin();
    
    for(; itor != arr.end(); itor++) {
        // cout << *itor << endl;
        if(before_element == -1) {
            before_element = *itor;
            answer.emplace_back(*itor);
        } else if (before_element == *itor) {
            continue;
        } else {
            before_element = *itor;
            answer.emplace_back(*itor);
        }
    }

    return answer;
}