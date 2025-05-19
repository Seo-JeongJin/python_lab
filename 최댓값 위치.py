
max_value = 0
row = 0
column = 0

for i in range(9):
    numbers = list(map(int, input().split()))
    for j in range(9):
        if numbers[j] > max_value:
            max_value = numbers[j]
            row = i + 1
            column = j + 1

print(max_value)
print(row, column)