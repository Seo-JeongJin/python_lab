
def student_score(name, **scores):
    print(f"{name}의 성적:")
    
    total = 0
    for score in scores.values():
        total += score
    
    for subject, score in scores.items():
        print(f" - {subject}: {score}점")
    
    print(f"총점: {total}점")
    
    return total

student_score("민수", math=90, english=85, science=88)