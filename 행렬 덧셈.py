
n, m = list(map(int, input().split()))

a = []
for _ in n:
    row = list(map(int, input().split()))
    a.append(row)
    
b = []
for _ in m:
    row = list(map(int, input().split()))
    b.append(row)
    
for i in range(n):
    row_sum = []
    for j in range(m):
        row_sum.append(a[i][j] + b[i][j])
        print(*row_sum)