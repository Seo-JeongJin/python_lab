
def is_secure_password(password):
    
    if len(password) < 8:
        return False       # 이 조건을 통과하지 못하면 바로 비밀번호가 안전하지 않다(else)로 이동, 조건 통과 시 그 다음 줄로 이동
    
    has_digit = any(char.isdigit() for char in password)
    
    has_upper = any(char.isupper() for char in password)
    
    return has_digit and has_upper

password = input("비밀번호를 입력하세요: ")

if is_secure_password(password):
    print("비밀번호가 안전합니다.")

else:
    print("비밀번호가 안전하지 않습니다.")





# def is_secure_password(password):
#     if len(password) >= 8:
#         return True          # 비밀번호의 길이가 여덟자 이상을 넘기만 하면 참이 되기 때문에 다음 줄을 무시 해버림림
    
#     has_digit = any(char.isdigit for char in password)
    
#     has_upper = any(char.isupper for char in password)
    
#     return has_digit and has_upper

# password = input("비밀번호를 입력하세요: ")

# if is_secure_password(password):
#     print("비밀번호가 안전합니다.")
# else:
#     print("비밀번호가 안전하지 않습니다.")
    
    ## return값을 반환한다는 것은 정의한 함수 자체가 return 값이 된다는 것!!