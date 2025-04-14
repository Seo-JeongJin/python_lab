
# def validate_reservation(age, event_code, reservation_date):
    
#     if event_code not in ['E1', 'E2', 'E3']:
#         return "잘못된 입력입니다. 프로그램을 종료합니다."
    
#     if not 1 <= reservation_date <= 30:
#         return "잘못된 입력입니다. 프로그램을 종료합니다."
    
#     if event_code == 'E1':
#         if age < 18:
#             return "나이 제한으로 인해 예약할 수 없습니다."
        
#     elif event_code == 'E2':
#         if reservation_date % 2 != 0:
#             return "선택하신 날짜에는 예약할 수 없습니다."
        
#     elif event_code == 'E3':
#         if age < 16:
#             return "나이 제한으로 인해 예약할수 없습니다."
#         if reservation_date % 7 != 0:
#             return "선택하신 날짜에는 예약할 수 없습니다."
        
#     return "예약이 완료되었습니다!" # 모든 조건을 통과했을 때 이 값을 반환
        
# age = int(input("나이를 입력하세요: "))
# event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
# reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# result = validate_reservation(age, event_code, reservation_date)

# print(result)





def validate_reservation(age, event_code, reservation_date):
    if event_code not in ["E1", "E2", "E3"]:
        return "잘못된 입력입니다. 프로그램을 종료합니다."
    if not 1 <= reservation_date <= 30:
        return "잘못된 입력입니다. 프로그램을 종료합니다."
    if event_code == "E1":
        if age < 18:
            return "나이 제한으로 인해 예약할 수 없습니다."
    elif event_code == "E2":
        if reservation_date % 2 != 0:
            return "선택하신 날짜에는 예약할 수 없습니다." 
    elif event_code == "E3":
        if age < 16:
            return "나이 제한으로 인해 예약할 수 없습니다."
        if reservation_date % 7 != 0:
            return "선택하신 날짜에는 예약할 수 없습니다."
    return "예약이 완료되었습니다!"   

age = int(input("나이를 입력하세요: "))
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

result = validate_reservation(age, event_code, reservation_date)

print(result)
    