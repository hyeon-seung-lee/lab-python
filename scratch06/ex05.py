"""
확률 변수(random variable):
    어떤 확률 분포와 연관되어 있는 변수
    (예) 동전 1개를 던지는 확률 분포에서, 동전 앞면의 개수 X
    P(X=1) = 1/2, P(X=0) = 1/2
    (예) 주사위 1개를 던지는 확률 분포에서, 주사위 눈의 개수 X
    X = 1, 2, 3, 4, 5, 6
기댓값(expected value):
    확률 변수의 확률에 확률 변수의 값을 가중 평균한 값
    E(X) = sum(x_i * P(X=x_i))
    (예) 동전 1개를 던질 때, 동전 앞면의 기댓값
    E = 1 * 1/2 + 0 * 1/2 = 1/2 = 0.5
    (예) 주사위 1개를 던질 때, 주사위 눈의 기댓값
    E = 1 * 1/6 + 2 * 1/6 + ... + 6 * 1/6 = 3.5

동전 3개를 던질 때, 확률 변수를 동전의 앞면의 개수
X = 0, 1, 2, 3
동전 3개를 10,000번 던지는 실험
-> P(X=0) = 1/8, P(X=1) = 3/8, P(X=2) = 3/8, P(X=3) = 1/8
-> 기대값 계산 (0*1 + 1*3 + 2*3 + 3*1)/8 = 1.5
"""
import random
from collections import Counter

event = [1, 0]
trials = 10_000
random.seed(1)
records = []
num_of_cases = 0
x_number = int(input('X = ? 의 숫자를 입력하세요: '))
expected_num = 0
expected_sum = 0

for i in range(trials):
    record = []
    for j in range(3):
        record.append(random.choice(event))
    records.append(tuple(record))

coin_event_counts = Counter(records)
print(coin_event_counts)

for event, count in coin_event_counts.items:
    if event[0] + event[1] + event[2] == x_number:
        num_of_cases += 1

p = num_of_cases / trials
print(f'P(X = {x_number}) = {p}')

for event, count in coin_event_counts.items:
    for k in range(4):
        expected_num = 0
        if event[0] + event[1] + event[2] == k:
            expected_num += 1
        expected_sum += expected_num * k
q = expected_sum / trials
print(f'기대값 : {q}')
