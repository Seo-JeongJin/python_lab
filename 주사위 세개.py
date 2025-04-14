
a, b, c = map(int, input().split())

# 같은 눈 3개
if a == b == c:
    print(10000 + a * 1000)
# 같은 눈 2개
elif a == b or b == c or c == a:
    if a == b:
        same = a
    elif b == c:
        same = b
    else:
        same = c
    print(1000 + same * 100)
# 서로 다른 눈
else:
    largest = a
    if largest < b:
        largest = b
    if largest < c:
        largest = c
    print(largest * 100)