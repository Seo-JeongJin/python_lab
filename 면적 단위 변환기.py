
def convert_to_square_feet(square_meters):
    ft = square_meters * 10.7639     # 1제곱미터 = 10.7639 ft**2
    return ft

def convert_to_acres(square_meters):
    ac = square_meters / 4046.86           # 1제곱미터 = 1 / 4046.86 ac 
    return ac

square_meters = float(input("토지의 면적을 제곱미터(m**2) 단위로 입력하세요: "))

result1 = convert_to_square_feet(square_meters)
result2 = convert_to_acres(square_meters)

if square_meters < 0:
    print("잘못된 입력입니다.")

else:
    print(f"{square_meters}제곱미터는 {result1} 평방피트입니다.")
    print(f"{square_meters}제곱미터는 {result2} 에이커입니다. ")

