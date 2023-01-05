x, y, w, h = map(int, input().split())

d = min(x, y, abs(w-x), abs(h-y))

print(d)