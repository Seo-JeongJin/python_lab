
import random

while True:
    n = int(input("Enter the number of dice rolls (between 100 and 1,000,000): "))
    
    if 10 <= n <= 1000000:
        break
    
    print("Please enter a number within the specified range.")

print("\nDice Roll Frequency Histogram")

# 눈금 나온 횟수 저장할 자료구조 생성
counts = [0, 0, 0, 0, 0, 0]
# 각 눈금 나온 횟수 세기
for i in range(n):
    result = random.randint(1, 6)
    counts[result - 1] += 1
# 가장 많이 나온 눈금 찾기
max_count = 0
for cell in counts:
    if cell > max_count:
        max_count = cell
# 히스토그램 출력
count = 1
for cell in counts:
    num_of_stars = cell * 10 // max_count
    star = ""
    for i in range(num_of_stars):
        star += "*"
    percent = cell / n * 100
    print(f"{count}: {star} ({cell} times, {percent:.2f}%)")
    count += 1