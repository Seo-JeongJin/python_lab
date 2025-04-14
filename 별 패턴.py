
N = int(input("숫자를 입력하세요: "))

for i in range(1, N + 1):
    print("*" * i)
for i in range(N - 1, 0, -1):  # -1 == "한 번 반복할 때마다 1씩 줄여라"
    print("*" * i)