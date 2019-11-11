"""
재귀 함수(recursive function)
"""

# factorial
# 0! = 1
# n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n


def factorial1(n: int) -> int:
    result = 1

    for x in range(1,n+1):
        result *= x
    return result


for x in range(6):
    print(f'{x}! = {factorial1(x)}')

print()


def factorial2(n: int) -> int:
    if n == 0:                  # 종료 조건
        return 1
    elif n > 0:
        return factorial2(n-1)*n


for x in range(6):
    print(f'{x}! = {factorial2(x)}')


# 1부터 n까지 더하는 함수

