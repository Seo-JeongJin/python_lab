
import random

count = int(input("리스트 개수를 입력하세요 (5 ~ 20): "))

if count > 20 or count < 5:
    print("오류 : 리스트 개수는 5 이상 20 이하여야 합니다.")
    exit()

created = [random.randint(1, 100) for _ in range(count)]

mean = sum(created) / count # 평균

deviation = [i - mean for i in created] # 편차 = 각 값 - 평균 -> 각 수가 평균과 얼마나 차이 나는지

variance = sum([i ** 2 for i in deviation]) / count # 분산 = 모든 편차^2의 합 / 데이터 개수 -> 전체 데이터의 퍼진 정도

standard_deviation = variance ** (1 / 2) # 표준편차 = 분산에 제곱근을 씌운 값

print(f"""
생성된 리스트 : {created}
평균 : {mean:.2f}
편차 : {[round(i, 2) for i in deviation]}
분산 : {variance:.2f}
표준편차 : {standard_deviation:.2f}""")