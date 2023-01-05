import sys
input = sys.stdin.readline
n = int(input())

number = [0] * 10001

for i in range(n):
    number[int(input())] += 1

for i in range(1, 10001):
    for j in range(number[i]):
        print(i)