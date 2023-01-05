import sys

input = sys.stdin.readline

N, M = map(int, input().split())

site = dict()

for i in range(N):
    a, b = map(str, input().rstrip('\n').split(' '))

    site.update({a:b})

for i in range(M):
    a = input().rstrip('\n')
    print(site.get(a))
