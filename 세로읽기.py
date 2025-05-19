
# 입력
# 총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 주어지는 글자는 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나이다. 각 줄의 시작과 마지막에 빈칸은 없다.

# 출력
# 영석이가 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다. 

# 예제 입력 1 
# ABCDE
# abcde
# 01234
# FGHIJ
# fghij
# 예제 출력 1 
# Aa0FfBb1GgCc2HhDd3IiEe4Jj
# 예제 입력 2 
# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx
# 예제 출력 2 
# Aa0aPAf985Bz1EhCz2W3D1gkD6x

lines = []

for _ in range(5):
    line = input()
    lines.append(line)

max_len = 0
for line in lines:
    if len(line) > max_len:
        max_len = len(line)

result = ""

for i in range(max_len):
    for j in range(5):
        if i < len(lines[j]):
            result += lines[j][i]