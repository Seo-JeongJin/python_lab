# 알람시계 45분 일찍 알람 설정하기

a, b = map(int, input().split())

if b >= 45:
    print(a, b - 45)
else:
    if a == 0:
        print(23, b + 15)
    else:
        print(a - 1, b + 15)
        

H, M = map(int, input().split())

M -= 45
if M < 0:
    M += 60
    H -= 1
    if H < 0:
        H = 23


print(H, M)