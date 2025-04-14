
a = int(input("첫 번째 수 입력: "))
b = int(input("두 번째 수 입력: "))
c = int(input("세 번째 수 입력: "))

if a == b == c:
    print("모든 수가 같습니다.")
elif a == b:
    print("두 수가 같습니다.", a, "와", b)
elif b == c:
    print("두 수가 같습니다.", b, "와", c)
elif c == a:
    print("두 수가 같습니다.", c, "와", a)
else:
    largest_num = a
    if b > largest_num:
        largest_num = b
    if c > largest_num:
        largest_num = c
    print("모든 수가 다릅니다. 가장 큰 수는", largest_num, "입니다.")        