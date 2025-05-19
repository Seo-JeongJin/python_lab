
text = "apple banana orange apple kiwi apple apple"

searching = input("찾을 문자열을 입력하세요: ")

words = []
word = ""
for char in text:
    if char != " ":
        word += char
    else:
        words.append(word)
        word = ""

if word:
    words.append(word)
    
position = []
count = 0
for i in range(len(words)):
    if searching == words[i]:
        count += 1
        position.append(i)
        
print(f"{searching}은 총 {count}번 등장합니다.")
print(f"위치 (인덱스): {position}")