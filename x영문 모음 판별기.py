
english = input("한 영문자를 입력하세요: ")

english = english.lower() # 입력된 영문자를 소문자로 전환(대소문자 구분 없앰)

vowel = ["a","e","i","o","u"]

if english in vowel:      # in 대신 == 를 사용하면 "a"와 ["a","e","i","o","u"]를 비교하는 것이기 때문에 항상 거짓이 된다.
    print(f"{english}은(는) 모음입니다.")
    
else:
    print(f"{english}은(는) 모음이 아닙니다.")    