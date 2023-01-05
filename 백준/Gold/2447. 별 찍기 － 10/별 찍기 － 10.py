def get_stars (matrix):
    setmatrix = []
    for i in range(3 * len(matrix)):
        if i // len(matrix) == 1:
            setmatrix.append(matrix[i % len(matrix)] + ' ' * len(matrix) + matrix[i % len(matrix)])
        else:
            setmatrix.append(matrix[i % len(matrix)] * 3)
    return setmatrix

star = ['***', '* *', '***']
q = int(input())
e = 0

while q != 3:
    q = q/3
    e += 1

for i in range(e):
    star = get_stars(star)

for i in star:
    print(i)