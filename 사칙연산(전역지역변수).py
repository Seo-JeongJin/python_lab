
# baseValue = 0

# def selectOperation():
#     global baseValue  # 전역 변수 참조

#     print("\n연산을 선택하세요:")
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 곱하기")
#     print("4. 나누기")

#     choice = input("선택 (1/2/3/4): ")
#     number = float(input("숫자를 입력하세요: "))

#     if choice == "1":
#         baseValue += number
#         print("결과:", baseValue)
#     elif choice == "2":
#         baseValue -= number
#         print("결과:", baseValue)
#     elif choice == "3":
#         baseValue *= number
#         print("결과:", baseValue)
#     elif choice == "4":
#         if number == 0:
#             print("에러: 0으로 나눌 수 없습니다.")
#         else:
#             baseValue /= number
#             print("결과:", baseValue)
#     else:
#         print("잘못된 선택입니다.")

# # 초기값 입력 받기
# try:
#     baseValue = float(input("초기값을 입력하세요: "))
#     selectOperation()
# except ValueError:
#     print("유효한 숫자를 입력해주세요.")
        
        
        
        
        
        
        
        
        
base_value = 0

def select_operation():
    global base_value
    
    base_value = float(input("기본 값을 입력하세요: "))
    
    print("1. 더하기\n2. 빼기\n3. 곱하기\n4. 나누기")
    
    select = int(input("선택(1/2/3/4): "))
    insult = float(input("숫자 입력: "))
    
    if select == 1:
        base_value += insult
        print(f"연산결과: {base_value}")
    elif select == 2:
        base_value -= insult
        print(f"연산결과: {base_value}")
    elif select == 3:
        base_value *= insult
        print(f"연산결과: {base_value}")
    elif select == 4:
       if insult == 0:
           print("에러: 0으로 나눌 수 없습니다.")
       else:
           base_value /= insult
           print(f"연산 결과: {base_value}")
           

select_operation()
    
        