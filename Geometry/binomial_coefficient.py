"""
이항계수
이항계수란 (x + y)^N 을 전개했을 때의 각 항의 계수를 의미한다.
이는 nC0 ~ nCn 으로 표시되고, 아래는 각 nCk를 구하기 위한 함수이다.
즉, 순열과 조합의 조합이다.

이는 다이나믹 프로그래밍 memoization 을 이용하여 구할 수 있다.
nCk = (n-1)C(k-1) + (n-1)Ck
이는 이항계수 트리를 그려보면 빠르게 이해가 된다
1
11
121
1331
...
"""


def binomial_coefficient(n, k):
    if k == 0 or k == n:
        memo[n][k] = 1
        return memo[n][k]
    if memo[n-1][k-1] == 0:
        memo[n-1][k-1] = binomial_coefficient(n-1, k-1)
    if memo[n-1][k] == 0:
        memo[n-1][k] = binomial_coefficient(n-1, k)
    return memo[n-1][k-1] + memo[n-1][k]


N, K = map(int, input().split())
memo = [[0] * (K + 1) for _ in range(N + 1)]
print(binomial_coefficient(N, K))
