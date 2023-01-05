N = int(input())

word = []

for _ in range(N):
    a = str(input())
    word.append(a)

word.sort(key=lambda user : (len(user), user))

for i in range(N):
    if i != N-1 and  word[i] == word[i+1]:
        continue
    else:
        print(word[i])
