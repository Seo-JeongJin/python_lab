
s = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

result = []

for a in alphabet:
    found = -1
    for i in range(len(s)):
        if s[i] == a:
            found = i
            break
    result.append(found)

print(" ".join(map(str, result)))