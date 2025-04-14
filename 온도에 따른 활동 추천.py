
temperature = float(input("현재 온도(섭씨)를 입력하세요: "))

print()

if temperature >= 30:
    print(f"현재 온도: {temperature}\n추천 활동: 수영")
elif temperature >= 20:
    print(f"현재 온도: {temperature}\n추천 활동: 등산")
elif temperature >= 10:
    print(f"현재 온도: {temperature}\n추천 활동: 자전거 타기")
else:
    print(f"현재 온도: {temperature}\n추천 활동: 스키")
