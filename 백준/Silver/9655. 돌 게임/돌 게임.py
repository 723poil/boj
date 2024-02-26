import sys

input = sys.stdin.readline

N = int(input())

max_n = N // 3 + N % 3

if max_n % 2 == 0:
    print('CY')
else:
    print('SK')