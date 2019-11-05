import numpy as np
from math import sqrt

# 빈 리스트(scores)를 선언
scores = []


# 난수 (0 <= x <= 100 ) 10개를 리스트에 저장

for i in range(10):
    scores.extend([np.random.randint(0,101)])
print(f'scores={scores}')

# 리스트에 저장된 시험 점수 10개의 총점을 계산, 출력
sum_score=0
for i in range(len(scores)):
    sum_score += scores[i]
print(f'sum:{sum_score}')

# 리스트에 저장된 시험 점수 10개의 평균을 계산, 출력
avg_score = sum_score/len(scores)
print(f'avg_score:{avg_score}')

# 표준 편차 계산
sum_score=0
stdev_score = 0

for i in range(len(scores)):
    sum_score += (scores[i]-avg_score)**2

stdev_score = sqrt(sum_score/len(scores))
print(f'stdev : {stdev_score}')

# 리스트에 저장된 시험 점수 10개 중에서 최대값, 최소값을 찾아서 출력

max_score = scores[0]

#최대값
for i in range(1,len(scores)):
    if max_score<scores[i]:
        max_score = scores[i]
    else:
        pass
print(f'max_score: {max_score}')

#최소값
min_score = scores[0]

#최대값
for i in range(1,len(scores)):
    if min_score>scores[i]:
        min_score = scores[i]
    else:
        pass
print(f'min_score: {min_score}')

