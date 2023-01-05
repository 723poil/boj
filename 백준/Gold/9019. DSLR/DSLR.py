import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def D(n):
    if n * 2 > 9999:
        return n*2 % 10000

    return n * 2

def S(n):
    if n - 1 == -1:
        return 9999
    
    return n - 1

def L(n):
    return n % 1000 * 10 + n // 1000

def R(n):
    return n % 10 * 1000 + n // 10
    
def BFS(A, B, dp):
    queue = deque()
    visited = ['n'] * 10000

    queue.append(A)

    while queue:
        number = queue.popleft()

        # dp-> visited로 방문했는지 확인
        # 사용한 함수 이름(DSLR)과 그 전 숫자 저장
        # B를 찾았을 경우 그 전 숫자 dp 검색하면서
        # 사용한 함수 이름들 list에 insert한 후 A까지 검색을 다 했을 경우
        # list 합쳐서 출력

        for i in range(4):
            if i == 0:
                N = D(number)
                if dp[N] == -1:
                    queue.append(N)
                    visited[N] = 'D'
                    dp[N] = number
            elif i == 1:
                N = S(number)
                if dp[N] == -1:
                    queue.append(N)
                    visited[N] = 'S'
                    dp[N] = number
            elif i == 2:
                N = L(number)
                if dp[N] == -1:
                    queue.append(N)
                    visited[N] = 'L'
                    dp[N] = number
            else:
                N = R(number)
                if dp[N] == -1:
                    queue.append(N)
                    visited[N] = 'R'
                    dp[N] = number
            if N == B:
                i = B
                a = deque()
                while i != A:
                    a.insert(0, visited[i])
                    i = dp[i]

                return ''.join(a)

for _ in range(T):
    A,B = map(int, input().split())
    dp = [-1] * 10000
    print(BFS(A,B, dp))