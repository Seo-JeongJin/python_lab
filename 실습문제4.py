
price_of_purchase = int(input("총 구매 금액: "))
num_of_refund = int(input("총 반품 횟수: "))
num_of_purchase = int(input("총 구매 횟수: "))
months_of_membership = int(input("가입 개월 수: "))

if num_of_purchase == 0:
    print("구매 횟수가 0입니다. 반품률을 계산할 수 없습니다.\n프로그램을 종료합니다.")
    exit()

if num_of_refund > num_of_purchase:
    print("반품 횟수가 구매 횟수보다 많을 수 없습니다.\n프로그램을 종료합니다.")
    exit()

refund_rate = (num_of_refund / num_of_purchase) * 100

if refund_rate >= 50 or (months_of_membership <= 3 and price_of_purchase <= 10000) or num_of_refund >= 10:
    result = "위험 고객"

elif refund_rate <= 10 and num_of_purchase >= 30 and price_of_purchase >= 2000000 and months_of_membership >= 12:
    result = "우수 고객"

else:
    result = "일반 고객"
    
print(f"반품률: {refund_rate:.1f}%")
print(f"결과: {result}")