
def validate_rrn(rrn):
    if len(rrn) > 13 or not rrn.isdigit(): # 주민번호가 아님을 판별
        return False
    
    check = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    
    total = 0
    for i in range(12):
        total += int(rrn[i]) * check[i]
    
    remain = total % 11
    last_place_value = (11 - remain) % 10
    
    return last_place_value == int(rrn[-1])

input_value = input("주민번호를 입력하세요: ")

if validate_rrn(input_value):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")
    
