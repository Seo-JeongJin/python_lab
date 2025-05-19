
import random

while True:
    n = int(input("Enter the number of dice rolls (between 100 and 1,000,000): "))
    
    if 100 <= n <= 1000000:
        break
    
    print("Please enter a number within the specified range.")
    
print("\nDice Roll Frequency Histogram: ")

counts = [0, 0, 0, 0, 0, 0] # 각 숫자가 나온 횟수를 저장할 리스트

for _ in range(n): # 주사위 던지기 반복문
    result = random.randint(1, 6)
    counts[result - 1] += 1
    
max_count = 0 # 가장 많이 나온 눈금의 횟수 찾기
for i in range(6):
    if counts[i] > max_count:
        max_count = counts[i]
        
for i in range(6):
    num_stars = int(counts[i] * 10 / max_count) # 해당 눈금이 얼마나 많이 나왔는지 상대적으로 별 개수 계산
    stars = ""
    for _ in range(num_stars):
        stars += "*"
    percentage = counts[i] * 100 / n
    print(f"{i + 1}: {stars} ({counts[i]} times, {percentage:.2f}%)")