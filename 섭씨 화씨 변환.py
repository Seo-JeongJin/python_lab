
def convert_celsius_to_fahrenheit(celsius):
    
    fahrenheit = celsius * 9/5 + 32
    
    return fahrenheit

celsius = float(input("섭씨 온도를 입력하세요: "))

fahrenheit = convert_celsius_to_fahrenheit(celsius)

print(f"화씨 온도는 {fahrenheit}입니다.")