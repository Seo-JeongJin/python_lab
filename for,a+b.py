
# t = int(input())

# for i in range(1, t + 1):
#     a, b = map(int, input().split())
    
#     print(a + b)

import sys

t = int(input())

for i in range(1, t + 1):
    # sys.stdin.readline() == input()과 동일하지만 끝에 개행문자(\n)를 포함하고 있다.
    # .rstrip() == 개행문자 제거
    a, b = map(int, sys.stdin.readline().rstrip().split())
    
    print(a + b)
    
    
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

# 예제 입력 1 
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2
# 예제 출력 1 
# Case #1: 2
# Case #2: 5
# Case #3: 7
# Case #4: 17
# Case #5: 7

t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().split())
    
    print(f"Case #{i}: {a + b}")
    
    
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

# 예제 입력 1 
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2
# 예제 출력 1 
# Case #1: 1 + 1 = 2
# Case #2: 2 + 3 = 5
# Case #3: 3 + 4 = 7
# Case #4: 9 + 8 = 17
# Case #5: 5 + 2 = 7

import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().rstrip().split())
    
    print(f"Case #{i}: {a} + {b} = {a + b}")