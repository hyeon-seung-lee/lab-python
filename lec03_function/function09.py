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

# 재귀함수를 이용한 하노이  탑
def hanoi_tower(n, start, target, aux):
    """
    재귀 함수를 사용해서 하노이 탑 문제 해결 방법 by Python

    :param n: 옮길 원반 겟수(자연수)
    :param start: 원반들이 있는 출발 기둥 번호
    :param target: 원반들을 모두 옮겨 놓을 타겟 기둥 번호
    :param aux: 보조 기둥
    :return: None
    """
    if n == 1 :
        print((f'{start} -> {target}'))
        return  # 함수 종료 부분


    # (n계의 원반을 보조 기둥(aux)
    # aux 기둥으로 모두 롬김

    # hanoi_tower(n , start, aux, target)

# 시작 기둥에 남아 있는 한계의 원반을 목표 금액으로 삼음.

# aux 기둥에 남아 있는 (n-1)개의 원반을
# start기둥을 보조 기둥으로 사용해서 target으로 옮김
    hanoi_tower(n-1, aux, target, start)

# 원반 한 개짜리 하노이 탑
hanoi_tower(n=1, start=1, target=3, aux = 2)
