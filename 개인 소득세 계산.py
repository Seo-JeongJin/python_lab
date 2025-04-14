
def calculate_tax(income):
    
    if income <= 10000:
        tax = income * 0.1
    
    elif 10000 < income <= 20000:
        tax = (income - 10000) * 0.15 + 1000
        
    else:
        tax = (income - 20000) * 0.2 + 2500
        
    return tax
    
income = float(input("소득 금액을 입력하세요: "))

tax = calculate_tax(income)

print(f"소득세는 {tax}달러 입니다.")                