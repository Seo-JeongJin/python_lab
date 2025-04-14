
def check_triangle_type(a, b, c):
    
    if a + b <= c or b + c <= a or c + a <= b:
        return "입력하신 변의 길이로는 삼각형을 만들 수 없습니다. 두 변의 합이 나머지 한 변의 길이보다 커야합니다."
    
    if a == b == c:
        return "입력하신 변의 길이로는 정삼각형을 만들 수 있습니다."
    
    elif a == b or b == c or c == a:
        return "입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다."
    
    else:
        return "입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다."
           
a = float(input("첫 번째 변의 길이를 입력하세요: "))    
b = float(input("두 번째 변의 길이를 입력하세요: "))    
c = float(input("세 번째 변의 길이를 입력하세요: "))

result = check_triangle_type(a, b, c)
print(result)