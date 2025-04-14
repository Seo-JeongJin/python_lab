
initial_capital = float(input("초기 자본금을 입력하세요: "))
buy_price = float(input("주식 가격을 입력하세요: "))
stock_count = float(input("구매할 주식 수를 입력하세요: "))
sell_price = float(input("판매할 때의 주식 가격을 입력하세요: "))

total_buy_cost = buy_price * stock_count

remaining_capital = initial_capital - total_buy_cost

total_sell_revenue = sell_price * stock_count

profit_or_loss = total_sell_revenue - total_buy_cost

print(f"구매 후 남은 자본금: {remaining_capital}")
print(f"예상 이익: {profit_or_loss}")

if profit_or_loss > 0:
    print(f"예상되는 이익입니다.")
elif profit_or_loss < 0:
    print(f"예상되는 손실입니다.")
else:
    print("손익이 없습니다.")