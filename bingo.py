
import random

while True:
    n = int(input("Enter the size of the bingo board (3 to 6): "))
    
    if 3 <= n <= 6:
        break
    
    print("Size must be between 3 and 6. Please try again.")
    
# 중복 제거
used = []

while len(used) < n * n:
    number = random.randint(1, 36)
    if number not in used:
        used.append(number)

# 중복 되지 않은 숫자들을 2차원 리스트로        
board = [used[i * n : (i + 1) * n] for i in range(n)]

# 초기 빙고 보드 출력
for row in board:
    for cell in row:
        print(str(cell).rjust(2), end=" ")
    print()
print()

# 게임 시작
count = 1
while True:
    count += 1
    random_number = random.randint(1, 36)
    input("\nPress Enter to generate a random number:")
    
    print(f"Random Number {count}: {random_number}")
    
    # 이전 빙고판의 별 확인
    for i in range(n):
        for j in range(n):
            if board[i][j] == random_number:
                board[i][j] = "*"
     
    for row in board:
        for cell in row:
            print(str(cell).rjust(2), end=" ")
        print()
    print()
    
    for i in range(n):
        is_bingo = True
        for j in range(n):
            if board[i][j] != "*":
                is_bingo = False
                break
        if is_bingo:
            bingo += 1
            
    for j in range(n): # 열 기준으로 행을 반복
        is_bingo = True
        for i in range(n):
            if board[i][j] != "*":
                is_bingo = False
                break
        if is_bingo:
            bingo += 1
    
    # 오 -> 왼 대각선
    is_bingo = True 
    for i in range(n):
        if board[i][i] != "*":
            is_bingo = False
            break
    if is_bingo:
        bingo += 1
        
    # 왼 -> 오 대각선
    is_bingo = True
    for i in range(n):
        if board[i][n - 1 - i] != "*":
            is_bingo = False
            break
    if is_bingo:
        bingo += 1
        
    
    if  is_bingo >= 2:
        print("Congratulations! You've won the game with 2 or more bingos!") 
        break
