
def calculate_attendance_score(hours_per_week, absence_hour, tardy_count):
    total_class_hours = hours_per_week * 15
    
    late_to_absent = tardy_count // 3 # // 연산자는 몫을 출력 ex) 5//3 == 2
    absence_hour += late_to_absent
    
    if absence_hour > total_class_hours * (1/4):
        return "학점 미부여"
    
    attendance_score = 20 - (20 * (absence_hour / total_class_hours))
    
    
    
    