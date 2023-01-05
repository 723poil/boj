#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    
    for(int i=0; i<sizes.size(); i++) {
        sort(sizes[i].begin(), sizes[i].end());
        cout << sizes[i][0] << ", ";
        cout << sizes[i][1] << endl;        
    }
    
    int garo = 0;
    int sero = 0;
    
    for(int i=0; i<sizes.size(); i++) {
        if(garo < sizes[i][0]) {
            garo = sizes[i][0];
        }
        if(sero < sizes[i][1]) {
            sero = sizes[i][1];
        }
    }
    
    answer = garo * sero;
    
    return answer;
}