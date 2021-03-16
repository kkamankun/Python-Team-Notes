"""
최대 공약수 & 최소 공배수
최대 공약수는 유클리드 호재법을 통해 아래와 같이 구할 수 있음
최소 공배수는 최대공약수를 이용해서 구하면 된다.
"""
import sys
from math import gcd


def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_lcm(a, b):
    return a * b // get_gcd(a, b)


a, b = map(int, sys.stdin.readline().rstrip().split())

# 직접 구현한 최대 공약수 최소 공배수
print(get_gcd(a, b))
print(get_lcm(a, b))

# 라이브러리 사용하는 최대 공약수 최소 공배수
print(gcd(a, b))
print(a*b//gcd(a, b))
