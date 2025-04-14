
while True:
    try:
        num = int(input("숫자를 입력하세요: "))

        if num % 2 == 0:    
            print(f"{num}은 짝수입니다.")   
        
        else:
            print(f"{num}은 홀수입니다.")

        break       
                               
    except ValueError:
        print("잘못된 입력입니다. 다시 입력해주세요")
            