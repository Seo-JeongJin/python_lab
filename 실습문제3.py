
korean_score = int(input("국어 점수: "))
english_score = int(input("영어 점수: "))
math_score = int(input("수학 점수: "))

avg_of_score = (korean_score + english_score + math_score) / 3

if korean_score >= 80 and english_score >= 80 and math_score >= 80 and avg_of_score >= 90:
    result = f"평균: {avg_of_score}\n결과: 우수 합격"
    
elif korean_score >= 40 and english_score >= 40 and math_score >= 40 and avg_of_score >= 70:
    result = f"평균: {avg_of_score}\n결과: 합격"

else:
    result = f"평균: {avg_of_score}\n결과: 불합격"

print(result)