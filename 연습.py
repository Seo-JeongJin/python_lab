
# 문제 설명:
# 사용자로부터 정수 n을 입력받아서,
# 1부터 n까지의 숫자 중 3 또는 5의 배수인 수들의 합을 구하세요.

# 🧠 예시:
# 입력: 10  
# 출력: 33   # (3 + 5 + 6 + 9 + 10)

n = int(input("입력: "))

total = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(f"3 또는 5의 배수인 수들의 합은 {total}입니다.")

# 문제 설명:
# 사용자로부터 문자열을 하나 입력받아서,
# 그 안에 들어있는 **모음(a, e, i, o, u)**의 개수를 세어보세요.
# (대소문자 구분 없이 처리)

# 🧠 예시:
# 입력: Hello World  
# 출력: 모음의 개수는 3개입니다.  (e, o, o)

input_value = input("입력: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for ch in input_value:
    if ch in vowels:
        count += 1

print(f"출력: {count}")



