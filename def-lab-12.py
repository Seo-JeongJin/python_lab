
def generate_profile(name, age, gender="미정", *interests, **metadata):
    
    print(f"""
[고객 프로필]
이름: {name}
나이: {age}
성별: {gender}""")
    
    if interests:
        print("관심사: ", end="")
        for i in range(len(interests)):
            print(interests[i], end=", " if i < len(interests) - 1 else "\n")
    
    if metadata:
        print("추가 정보: ", end="")
        items = list(metadata.items())
        for i in range(len(items)):
            key, value = items[i]
            print(f"{key}={value}", end=", " if i < len(items) - 1 else "\n")

generate_profile("홍길동", 30)
generate_profile("지민", 26, "여성", *["여행", "사진", "독서"], job="디자이너", country="한국")