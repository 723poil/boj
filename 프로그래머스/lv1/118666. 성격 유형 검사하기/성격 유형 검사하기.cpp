#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
// #include <algorithm>


using namespace std;

int firstScore = 0;  // R (-), T (+)
int secondScore = 0; // C (-), F (+)
int thirdScore = 0;  // J (-), M (+)
int fourthScore = 0; // A (-), N (+) 

void calScore(char mbti, int score);

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    
    int score[8] = {0, 3, 2, 1, 0, 1, 2, 3};
    
    for(int i=0; i < survey.size() ; i++) {
        cout << survey[i] << endl;
        if(choices[i] < 4) {            
            calScore(survey[i][0], score[choices[i]]);
        } else if (choices[i] > 4) {
            calScore(survey[i][1], score[choices[i]]);
        }
    }
    
    if(firstScore > 0) {
        answer = "T";
    } else {
        answer = "R";
    }
    
    if(secondScore > 0) {
        answer += "F";
    } else {
        answer += "C";
    }
    
    if(thirdScore > 0) {
        answer += "M";
    } else {
        answer += "J";
    }
    
    if(fourthScore > 0) {
        answer += "N";
    } else {
        answer += "A";
    }
    
    return answer;
}

void calScore(char mbti, int score) {
    switch(mbti) {
        case 'R': 
            firstScore -= score;
            break;
        case 'T':
            firstScore += score;
            break;
        case 'C':
            secondScore -= score;
            break;
        case 'F':
            secondScore += score;
            break;
        case 'J':
            thirdScore -= score;
            break;
        case 'M':
            thirdScore += score;
            break;
        case 'A':
            fourthScore -= score;
            break;
        case 'N':
            fourthScore += score;
            break;
    }
}