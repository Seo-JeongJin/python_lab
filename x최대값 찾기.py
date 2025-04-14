
#ChatGPT
# num1 = int(input("첫 번째 숫자를 입력하세요: "))

# num2 = int(input("두 번째 숫자를 입력하세요: "))

# num3 = int(input("세 번째 숫자를 입력하세요: "))

# largest = num1

# if num2 > largest:
#     largest = num2
    
# if num3 > largest:
#     largest = num3
    
# print(f"가장 큰 숫자는 {largest}입니다.")                    



#ME
num1 = int(input("첫 번째 숫자를 입력하세요: "))

num2 = int(input("두 번째 숫자를 입력하세요: "))

num3 = int(input("세 번째 숫자를 입력하세요: "))

if num1 >= num2 and num1 >= num3:   # >=에서 =가 없으면 각 숫자가 5,5,3이 나왔을 때 조건문이 false가 되므로 다음 단계로 넘어감, 등호가 있으면 num1이 출력되겠지
    print(f"가장 큰 숫자는 {num1}입니다.")

elif num2 >= num1 and num2 >= num3:
    print(f"가장 큰 숫자는 {num2}입니다.")
    
else:
    print(f"가장 큰 숫자는 {num3}입니다.")        
