
import random

table = int(input("테이블 개수 입력: "))
row = int(input("행 수 입력: "))
col = int(input("열 수 입력: "))

option = int(input("""
출력 옵션을 선택하세요: 
1. 1부터 시작하여 열 방향으로 증가
2. 1 ~ 100 사이 랜덤 값 출력
옵션 (1 또는 2): """))

shape = int(input("""
출력 형태를 선택하세요: 
1. 테두리만 출력
2. 왼쪽 -> 오른쪽 대각선 출력
3. 오른쪽 -> 왼쪽 대각선 출력
4. 양방향 대각선 출력
출력 형태 옵션 (1 ~ 4): """))

for t in range(table):
    print(f"\n테이블 {t + 1}")
    
    count = 1
    
    for i in range(row):
        for j in range(col):
            
            value = count if option == 1 else random.randint(1, 100)
            
            if shape == 1:
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    print(value, end="\t")
                else:
                    print(" ", end="\t")
                    
            elif shape == 2:
                if i == j:
                    print(value, end="\t")
                else:
                    print(" ", end="\t")
                    
            elif shape == 3:
                if j == col - 1 - i:
                    print(value, end="\t")
                else:
                    print(" ", end="\t")
            
            elif shape == 4:
                if i == j or j == col - 1 - i:
                    print(value, end="\t")
                else:
                    print(" ", end="\t")
            
            count += 1
        print()
                