
a = int(input())
b = int(input())
c = int(input())

result = a * b * c

count = [0 * i for i in range(len(str(result)))]

for number in str(result):
    count[int(number)] += 1
    
for i in count:
    print(i)