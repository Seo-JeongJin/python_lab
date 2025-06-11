
def calculate_average(*args):
    if len(args) == 0: # 함수는 입력 인자가 0개여도 호출 가능 하기 때문
        return 0       # 입력 값, 출력 값 모두 optinal(선택)
    
    total = 0
    for val in args: # *args는 함수 내부에서 tuple 타입이므로 iterable
        total += val
    
    avg = total / len(args)
    
    return avg

print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))