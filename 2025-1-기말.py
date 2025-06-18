
students = {}  

def input_student():
    std_id = int(input("학번 입력: "))  
    if std_id in students:
        print("이미 등록된 학번입니다.")
        return

    name = input("이름 입력: ")
    kor = int(input("국어 성적 입력: "))
    eng = int(input("영어 성적 입력: "))
    math = int(input("수학 성적 입력: "))

    total = kor + eng + math
    avg = total / 3

    students[std_id] = {
        "이름": name,
        "국어": kor,
        "영어": eng,
        "수학": math,
        "합계": total,
        "평균": avg
    }

    print("성적이 저장되었습니다.")

def print_all_students():
    if not students:
        print("등록된 학생이 없습니다.")
        return

    print("\n[ 전체 학생 성적 ]")
    print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
    for std_id, info in students.items():
        print(f"{std_id}\t{info['이름']}\t{info['국어']}\t{info['영어']}\t{info['수학']}\t{info['합계']}\t{info['평균']:.2f}")

def search_student():
    std_id = int(input("조회할 학번을 입력: "))
    if std_id in students:
        print(f"""
[ 학생 정보 ]
학번: {std_id}
이름: {students[std_id]['이름']}
국어: {students[std_id]['국어']}
영어: {students[std_id]['영어']}
수학: {students[std_id]['수학']}
합계: {students[std_id]['합계']}
평균: {students[std_id]['평균']:.2f}""")
        
    else:
        print("해당 학번의 학생 정보가 없습니다.")

def delete_student():
    std_id = int(input("삭제할 학번을 입력: "))
    if std_id in students:
        del students[std_id]
        print("학생 정보가 삭제되었습니다.")
    else:
        print("해당 학번의 학생 정보가 없습니다.")

def main():
    while True:
        print("""
===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료""")

        choice = input("메뉴를 선택하세요 (1~5): ")

        if choice == '1':
            input_student()
        elif choice == '2':
            print_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~5 사이의 숫자를 선택하세요.")

main()