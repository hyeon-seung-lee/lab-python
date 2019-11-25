import random
from collections import Counter

experiments = []
coin = (1, 0)
trials = 10_000
for _ in range(trials):
    heads = 0  # 동전 앞면의 개수
    for _ in range(3):
        heads += random.choice(coin)
    experiments.append(heads)
print(experiments[0:10])

head_counts = Counter(experiments)
print(head_counts)

expected_value = 0
for x, cnt in head_counts.items():
    expected_value += x * cnt / trials
print('기댓값 : ', expected_value)

# 주사위 눈의 기댓값
dice = (1, 2, 3, 4, 5, 6)
experiments = [random.choice(dice) for _ in range(trials)]
print(experiments[0:10])
head_counts = Counter(experiments)
print(head_counts)
expected_value = 0
for x, cnt in head_counts.items():
    expected_value += x * cnt / trials
print('주사위 눈의 기댓값 =', expected_value)
