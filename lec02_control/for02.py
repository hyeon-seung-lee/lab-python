from random import seed

import numpy as np
from math import sqrt

# 빈 리스트(scores)를 선언
scores = []


# 난수 (0 <= x <= 100 ) 10개를 리스트에 저장

for i in range(10):
    scores.extend([np.random.randint(0, 101)])
print(f'scores={scores}')

# 리스트에 저장된 시험 점수 10개의 총점을 계산, 출력
sum_score = 0
'''
for i in range(len(scores)):
    sum_score += scores[i]

'''
for score in scores:
    sum_score += score

print(f'sum:{sum_score}')
print(f'sum2: {sum(scores)}') # sum 함수를 이용한 총점 계산

# 리스트에 저장된 시험 점수 10개의 평균을 계산, 출력
avg_score = sum_score/len(scores)
print(f'avg_score:{avg_score}')
print(f'avg_score2:{np.mean(scores)}')  # numpy의 mean 함수를 이용한 평균 계산
# 표준 편차 계산
sum_score = 0
stddev_score = 0

'''
for i in range(len(scores)):
    sum_score += (scores[i]-avg_score)**2
'''
for score in scores:
    sum_score += (score-avg_score)**2

stddev_score = sqrt(sum_score/(len(scores)))
print(f'stddev : {stddev_score}')
print(f'stddev2 : {np.std(scores)}')

# 리스트에 저장된 시험 점수 10개 중에서 최대값, 최소값을 찾아서 출력

max_score = scores[0]
min_score = scores[0]
'''
# 최대값
for i in range(1,len(scores)):
    if max_score<scores[i]:
        max_score = scores[i]
    else:
        pass
# 최소값


for i in range(1,len(scores)):
    if min_score>scores[i]:
        min_score = scores[i]
    else:
        pass
'''
for score in scores:
    if score > max_score:
        # 리스트에서 현재 최댓값보다 더 큰 수를 찾은 경우
        max_score = score
    if score < min_score:
        # 리스트에서 현재 최솟값보다 더 작은 수를 찾은 경우
        min_score = score

print(f'max_score: {max_score}')
print(f'max_score2: {max(scores)}') # max 함수를 이용한 최대값
print(f'min_score: {min_score}')
print(f'max_score2: {min(scores)}') # min 함수를 이용한 최대값


sorted_scores = sorted(scores)
print(sorted_scores)
print(scores)


