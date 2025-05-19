
price = int(input("상품 가격을 입력하세요: "))

if price >= 100000:
    discount_rate = 0.1

elif price >= 50000:
    discount_rate = 0.05

else:
    discount_rate = 0
    
discount_price = price * discount_rate
final_price = price - discount_price

print(f"""할인율: {int(discount_rate * 100)}%
할인 금액: {int(discount_price)}원
최종 결제 금액: {int(final_price)}원""")