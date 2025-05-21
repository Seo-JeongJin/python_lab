
a = int(input())
b = int(input())
c = int(input())

result = a * b * c

count = [0 * i for i in range(10)] # 0부터 9까지의 숫자가 몇번 등장 했는지 저장하는 리스트

for number in str(result):
    count[int(number)] += 1
    
for i in count:
    print(i)