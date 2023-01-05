N, M = map(int, input().split())
t = list(map(int, input().split()))

left = 1
right = max(t)
while left <= right:
    mid = (left + right) // 2

    sum = 0

    for i in t:
        if i - mid > 0:
            sum += i - mid
        if sum >= M:
            break

    if sum >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)