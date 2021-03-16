"""
N 까지의 모든 Prime Number(소수)를 찾기 위한 알고리즘
에라토스테네스의 체 -> O(N * log( log(N) ) )
Input: Size N
Output: Prime Number List
"""


# 에라토스테네스의 체
def prime_sieve(sieve_size):
    # 0~N 까지의 공간
    sieve = [True] * (sieve_size + 1)
    # 0과 1은 소수가 아니므로 제외
    sieve[0] = False
    sieve[1] = False
    # 2부터 sqrt(N) + 1 까지의 숫자를 탐색
    for i in range(2, int(sieve_size**0.5) + 1):
        # i가 소수가 아니라면 패스
        if sieve[i] is False:
            continue
        # i가 소수라면 i^2 부터 i의 배수들을 모두 소수에서 제외
        for j in range(i**2, sieve_size+1, i):
            sieve[j] = False
    # True 만 골라서 소수 리스트로 생성
    primes = []
    for i in range(sieve_size + 1):
        if sieve[i]:
            primes.append(i)
    return primes


N = int(input())
prime_list = prime_sieve(N)
print(prime_list)
