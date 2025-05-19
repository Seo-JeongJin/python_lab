
# 알고리즘
# 1. 음료 기본 가격 설정
# 2. 크기별 추가 요금 계산
# 3. 기본 + 추가 요금 계산
# 4. 멤버십 고객이면 10% 할인 적용
# 5. 멤버십 고객이면서 커피/라떼 + large 사이즈일 경우 무료 샷 제공

# 사용자로부터 음료, 크기, 멤버십 여부 입력 받기
drink = input("음료를 선택하세요 (coffee/latte/juice): ").lower()
size = input("크기를 선택하세요 (small/medium/large): ").lower()
membership = input("멤버십 이신가요? (yes/no): ").lower()

# 음료 기본 가격 설정
if drink == "coffee":
    price = 3000
elif drink == "latte":
    price = 4000
elif drink == "juice":
     price = 3500
    
# 크기별 추가 요금 계산
if size == "small":
    add_price = 0
elif size == "medium":
    add_price = 500
elif size == "large":
    add_price = 1000

# 기본 + 추가 요금 계산
total_price = int(price + add_price)
free_shot = False

# 멤버쉽 고객이면 10% 할인 적용
if membership == "yes":
    discount = int(total_price * (1 / 10))
    total_price = total_price - discount
    discount_display = str(discount) + "원"
    if (drink == "coffee" or drink == "latte") and size == "large":
        free_shot = True
elif membership == "no":
    discount = "할인 없음"
    discount_display = discount

result = f"""
음료 가격: {price}원
크기 추가 요금: {add_price}원
할인 적용: {discount_display}
최종 결제 금액: {total_price}원"""
print(result)

if free_shot:
    print("무료 샷이 제공됩니다!")