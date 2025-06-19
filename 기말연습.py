
# # 기말 대비
# students = {}

# def input_student(students):
#     std_id = int(input("학번 입력: "))
#     if std_id in students:
#         print("이미 등록된 학번입니다.")
#         return
    
#     name = input("이름 입력: ")
#     kor = int(input("국어 성적 입력: "))
#     eng = int(input("영어 성적 입력: "))
#     math = int(input("수학 성적 입력: "))
    
#     total = kor + eng + math
#     avg = total / 3
    
#     students[std_id] = {
#         "이름":name,
#         "국어":kor,
#         "영어":eng,
#         "수학":math,
#         "합계":total,
#         "평균":avg
#     }
    
#     print("성적이 저장되었습니다.")

# def print_all_students(students):
#     if not students:
#         print("저장된 학생 정보가 없습니다.")
#         return
    
#     print("\n[ 전체 학생 성적 ]")
#     print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
#     for std_id, info in students.items():
#         print(f"{std_id}\t{info["이름"]}\t{info["국어"]}\t{info["영어"]}\t{info["수학"]}\t{info["합계"]}\t{info["평균"]:.2f}")

# def search_student(students):
#     std_id = int(input("조회할 학번 입력: "))
#     if std_id not in students:
#         print("해당 학번의 학생 정보가 없습니다.")
#         return
#     else:
#         print(f"""
# [ 학생 정보 ]
# 학번: {std_id}
# 이름: {students[std_id]["이름"]}
# 국어: {students[std_id]["국어"]}
# 영어: {students[std_id]["영어"]}
# 수학: {students[std_id]["수학"]}
# 합계: {students[std_id]["합계"]}
# 평균: {students[std_id]["평균"]:.2f}""")

# def delete_student(students):
#     std_id = int(input("삭제할 학번 입력: "))
#     if std_id not in students:
#         print("해당 학번의 학생 정보가 없습니다.")
#     else:
#         del students[std_id]
#         print("학생 정보가 삭제되었습니다.")

# def main():
#     while True:
#         print("""
# ===== 학생 성적 관리 프로그램 =====
# 1. 학생 성적 입력
# 2. 학생 성적 출력
# 3. 학생 성적 확인
# 4. 학생 성적 삭제
# 5. 종료""")
        
#         choice = int(input("메뉴 선택 (1~5): "))
        
#         if choice == 1:
#             input_student(students)
#         elif choice == 2:
#             print_all_students(students)
#         elif choice == 3:
#             search_student(students)
#         elif choice == 4:
#             delete_student(students)
#         elif choice == 5:
#             print("프로그램을 종료합니다.")
#             break
#         else:
#             print("잘못된 입력입니다. 1~5 사이의 숫자를 선택하세요.")

# main()


# # lab 11
# def add_numbers(*args, **kwargs):
    
#     options = ["abs", "only_even", "unique"]
    
#     for key in kwargs:
#         if key not in options:
#             print(None)
#             return
        
#     values = list(args)
    
#     if "abs" in kwargs and kwargs["abs"] == True:
#         for idx, val in enumerate(values):
#             if val < 0:
#                 values[idx] = -val
    
#     if "only_even" in kwargs and kwargs["only_even"] == True:
#         values = [val for val in values if val % 2 == 0]
    
#     if "unique" in kwargs and kwargs["unique"] == True:
#         temp = []
#         for val in values:
#             if val not in temp:
#                 temp.append(val)
#         values = temp
        
#     total = 0
#     for val in values:
#         total += val
    
#     print(f"합계는 {total}입니다.")

# add_numbers(1, -2, 2, -3)
# add_numbers(1, -2, 2, -3, abs=True, only_even=True)
# add_numbers(1, 2, 2, 3, 3, 4, unique=True)
# add_numbers(1, 2, 3, round=True)


# # lab 12
# def generate_profile(name, age, gender="미정", *interests, **metadata):
    
#     print(f"""
# [고객 프로필]
# 이름: {name}
# 나이: {age}
# 성별: {gender}""")
    
#     if interests:
#         print("관심사: ", end="")
#         for i in range(len(interests)):
#             print(interests[i], end=", " if i < len(interests) - 1 else "\n")
    
#     if metadata:
#         print("추가 정보: ", end="")
#         items = list(metadata.items())
#         for i in range(len(items)):
#             key, value = items[i]
#             print(f"{key}={value}", end=", " if i < len(items) - 1 else "\n")
#         print(items)

# generate_profile("홍길동", 30)
# generate_profile("지민", 26, "여성", *["여행", "사진", "독서"], job="디자이너", country="한국")



# # 2024 1학기 기말
import random

while True:
    n = int(input("Enter the size of the bingo board (3 to 6): "))
    
    if 3 <= n <= 6:
        break
    
    print("Size must be between 4 and 6. Please try again.")
    
used = []
while len(used) < n * n:
    num = random.randint(1, 36)
    if num not in used:
        used.append(num)

board = used[:]

print("Initial Bingo Board")
for i in range(n):
    for j in range(n):
        num = board[i * n + j]
        print(str(num).rjust(2), end=" ")
    print()
    
count = 0

while True:
    count += 1
    input("\nPress Enter to generate a random number: ")
    rand_num = random.randint(1, 36)
    print(f"Random Number {count}: {rand_num}")
    
    for i in range(n * n):
        if board[i] == rand_num:
            board[i] = "*"
    
    for i in range(n):
        for j in range(n):
            num = board[i * n + j]
            print(str(num).rjust(2), end=" ")
        print()

    bingo = 0
    
    for i in range(n):
        is_bingo = True
        for j in range(n):
            if board[i * n + j] != "*":
                is_bingo = False
                break
        if is_bingo:
            bingo += 1
    
    for j in range(n):
        is_bingo = True
        for i in range(n):
            if board[i * n + j] != "*":
                is_bingo = False
                break
        if is_bingo:
            bingo += 1
        
    is_bingo = True
    for i in range(n):
        if board[i * (n + 1)] != "*":
            is_bingo = False
            break
    if is_bingo:
        bingo += 1
    
    is_bingo = True
    for i in range(n):
        if board[(i + 1) * (n - 1)] != "*":
            is_bingo = False
            break
    if is_bingo:
        bingo += 1
    
    if bingo >= 2:
        print("Congratulations! You've won the game with 2 or more bingos!")
        break