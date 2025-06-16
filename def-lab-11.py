
# *args == 정수 여러 개 받음, **kwargs == 옵션 받음
def add_nums(*args, **kwargs):
    
    # 허용된 옵션들만 모음
    valid_options = {"abs", "only_even", "unique"}
    
    # kwargs에 이상한 키가 들어가 있으면 None 출력 후 종료
    for key in kwargs:
        if key not in valid_options:
            print(None)
            return
    
    # 모든 옵션 기본 값을 False로 시작
    options = {"abs" : False, "only_even" : False, "unique" : False}
    
    # 실제 kwargs에 받은 옵션이 있으면 그걸로 덮어씀
    # ex) kwargs = {"abs" : True} -> options["abs"] = True
    for key in options:
        options[key] = kwargs.get(key, False)
    
    # *args를 list로 복사
    numbers = list(args)
    
    # 중복 제거 직접 구현
    # unique_numbers는 중복 없이 저장된 최종 리스트
    if options["unique"]:
        unique_numbers = []
        for n in numbers:
            if n not in unique_numbers:
                unique_numbers.append(n)
        numbers = unique_numbers
    
    # 절댓값 처리
    if options["abs"]:
        numbers = [n if n >= 0 else -n for n in numbers]
    
    # 짝수 필터링
    if options["only_even"]:
        numbers = [n for n in numbers if n % 2 == 0]
    
    # 합계 계산
    total = 0
    for n in numbers:
        total += n
    
    print(f"합계는 {total}입니다.")

add_nums(1, -2, 2, -3)
add_nums(1, -2, 2, -3, abs=True, only_even=True)
add_nums(1, 2, 2, 3, 3, 4, unique=True)
add_nums(1, 2, 3, round=True)