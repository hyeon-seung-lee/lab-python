import random
from collections import Counter

coin = ['H', 'T']
trials = 10000


def experiment(type, n, t):
    """

    :param type: 실험 타입(동전 던지기 or 주사위 던지기)
    :param n: 동전의 개수
    :param t: 실험 회수
    :return: 리스트
    """
    cases = []  # 동전 던지기 실험 결과를 저장할 리스트
    for _ in range(t):  # 실험 회수 만큼 반복
        case = []  # 각 실험의 결과를 저장
        for _ in range(n):  # 동전 개수만큼 반복
            rand = random.choice(type)  # 'H' or 'T'
            case.append(rand)  # 1회 실험 결과에 저장
        # 1회 실험이 끝날 때마다 각 실험 결과를 tuple로 저장
        # Counter 클래스는 tuple의 개수는 셀수 있지만, list의 개수는 셀 수 없음
        cases.append(tuple(case))
    return cases


coin_exp = experiment(coin, 2, 10000)
print(coin_exp[0:10]) # 첫 10개의 실험 결과 확인
coin_event_counts = Counter(coin_exp)
print( coin_event_counts)


def how_many_heads(x):
    counter = Counter(x)
    return counter['H']

num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if how_many_heads(ev) ==1:
        num_of_cases += cnt

p_h1 = num_of_cases / trials
print('P(앞면이 1개일 확률', p_h1)

