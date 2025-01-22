matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

m,n = 0,0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            m = i
            n = j


print(abs(2-m)+abs(2-n))
