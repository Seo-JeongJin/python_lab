
def calculate_average(math_score, science_score, english_score):
    average = (math_score + science_score + english_score) / 3
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return average, grade   # return은 변수 반환을 한꺼번에 처리할 수 있다?  

math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))

average, grade = calculate_average(math_score, science_score, english_score)

# grade, average = calculate_average(math_score, science_score, english_score)  ==> grade에 숫자가 들어가고 average에 학점이 들어가버린다, return 값의 순서에 따라서 달라진다. return grade, average로 값을 반환했으면 알맞게 된다.

# average = calculate_average(math_score, science_score, english_score)
# grade = calculate_average(math_score, science_score, english_score)       ==> 이렇게 하면 각각 함수의 반환값(average, grade)즉, 튜플 전체를 할당해버림 

print(f"평균 점수는 {average}이고, 학점은 {grade}입니다.")