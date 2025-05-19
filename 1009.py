
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    n = a ** b
    k = n % 10
    print(k)