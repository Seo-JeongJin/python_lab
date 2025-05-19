
user = int(input("총 사용자 수를 입력하세요: "))

for i in range(user):
    initial_balance = 100000
    print(f"\n[{i + 1}번째 사용자] 초기 잔액: {initial_balance}원")
    
    while initial_balance > 0:
        print(f"현재 잔액: {initial_balance}원")
        
        withdrawal_amount = int(input("인출할 금액을 입력하세요 (0 입력 시 종료): "))
    
        if withdrawal_amount == 0:
            print(f"{i + 1}번 사용자 인출이 종료되었습니다.")
            break
            
        if withdrawal_amount not in [50000, 10000, 5000, 1000]:
            print("인출 단위는 50,000 / 10,000 / 5,000 / 1,000원만 가능합니다.")
            continue
        
        if withdrawal_amount > initial_balance:
            print("잔액이 부족합니다.")
            continue
        
        initial_balance -= withdrawal_amount
        print(f"출금 완료: {withdrawal_amount}원")
        
        if initial_balance == 0:
            print(f"잔액이 모두 소진되었습니다.\n{i + 1}번 사용자 인출이 종료되었습니다.")
            break

print("\n모든 사용자의 인출이 완료되었습니다. 프로그램을 종료합니다.")