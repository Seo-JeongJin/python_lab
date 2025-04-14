# # 개인 소득세
# def calculate_tax(income):
    
#     if income <= 10000:
#         tax = income * 0.1
    
#     elif 10000 < income <= 20000:
#         tax = (income - 10000) * 0.15 + 1000
        
#     else:
#         tax = (income - 20000) * 0.2 + 2500
    
#     return tax

# income = float(int(input("소득 금액을 입력하세요: ")))

# tax = calculate_tax(income)

# print(f"소득세는 {tax}달러 입니다.")    



# 섭씨 화씨 변환
# def convert_celsius_to_fahrenheit(celsius):
    
#     fahrenheit = celsius * 9/5 + 32
    
#     return fahrenheit

# celsius = float(input("섭씨 온도를 입력하세요: "))

# fahrenheit = convert_celsius_to_fahrenheit(celsius)

# print(f"화씨 온도는 {fahrenheit}입니다.")



# 최대값 찾기
# def max_value(a, b, c):
#     max_val = a
    
#     if b > max_val:
#         max_val = b
        
#     if c > max_val:
#         max_val = c
    
#     return max_val        

# a = float(input("첫 번째 숫자를 입력하세요: "))            
# b = float(input("두 번째 숫자를 입력하세요: "))            
# c = float(input("세 번째 숫자를 입력하세요: "))

# result = max_value(a, b, c)

# print(f"가장 큰 숫자는 {result}입니다.")



# 방향 명령어 해석
# direction = input("방향을 입력하세요(left, right, up, down): ")

# if direction == "left":
#     print("왼쪽으로 이동합니다.")

# elif direction == "right":
#     print("오른쪽으로 이동합니다.")
    
# elif direction == "up":
#     print("위로 이동합니다.")
    
# elif direction == "down":
#     print("아래로 이동합니다.")                        
    
# else:      # else는바로 앞에 있는 if 조건문과만 연결된다.
#     print("알 수 없는 명령어 입니다.")               



# 영문 모음 판별기
# text = input("한 문자를 입력하세요: ")

# vowel = ["a", "e", "i", "o", "u"]

# if text in vowel:
#         print(f"{text}는 모음입니다.")
        
# else:
#     print(f"{text}는 모음이 아닙니다.")



# 사칙연산 계산기

num1 = float(input("첫 번째 숫자를 입력하세요: "))        
num2 = float(input("두 번째 숫자를 입력하세요: "))

sum = num1 + num2
sub = num1 - num2
kake = num1 * num2
wari = num1 / num2

print(f"합: {sum}")        
print(f"차: {sub}")        
print(f"곱: {kake}")        
print(f"나눔: {wari}")        