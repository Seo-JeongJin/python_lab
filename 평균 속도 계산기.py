
depart_hour = int(input("출발 시(시간)를 입력하세요: "))
depart_minute = int(input("출발 시(분)를 입력하세요: "))
arrive_hour = int(input("도착 시(시간)를 입력하세요: "))
arrive_minute = int(input("도착 시(분)를 입력하세요: "))
distance = int(input("이동 거리(km)를 입력하세요: "))

total_travel_time = (((arrive_hour * 60 + arrive_minute) - (depart_hour * 60 + depart_minute)) / 60)

average = distance / total_travel_time

print()

print(f"이동 거리: {distance}km")
print(f"출발 시간: {depart_hour}시 {depart_minute}분")
print(f"도착 시간: {arrive_hour}시 {arrive_minute}분")
print(f"평균 속도: {average}km/h")

if average >= 90:
    print("속도 상태: 빠름")
elif average >= 60:
    print("속도 상태: 보통")
else:
    print("속도 상태: 느림")