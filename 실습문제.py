
choice = int(input("""
도형을 선택하세요:
1. 원의 면적
2. 삼각형의 면적 계산
3. 사각형의 면적 계산
>> """))

if choice == 1:
    r = int(input("반지름을 입력하세요: "))
    result = f"원의 면적은 {3.14 * (r ** 2)}"
    
elif choice == 2:
    bottom = int(input("밑변을 입력하세요: "))
    height = int(input("높이를 입력하세요: "))
    result = f"삼각형의 면적은 {(bottom * height) / 2}"

elif choice == 3:
    bottom = int(input("가로를 입력하세요: "))
    height = int(input("세로를 입력하세요: "))
    result = f"사각형의 면적은 {bottom * height}"

else:
    result = "잘못된 입력입니다."
    
print(result)