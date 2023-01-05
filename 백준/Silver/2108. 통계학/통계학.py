import sys
from statistics import multimode
input = sys.stdin.readline

N = int(input())

number = []

for _ in range(N):
    number.append(int(input()))

s = sum(number)
number.sort()

print(int(round(s / N, 0)))
print(number[N//2])

modes = multimode(number)

if len(modes)>1:
    mode = modes[1]
else:
    mode = modes[0]

print(mode)
print(number[-1]-number[0])