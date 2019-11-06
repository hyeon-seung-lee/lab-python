"""
for-in 구문연습2

# 피보나치 수열(fibonacci sequence)
seq = [0, 1]

for i in range(1,20):
    seq.append(seq[i]+seq[i-1])

for j in range(len(seq)):
    print(f'seq({j}): {seq[j]}')
"""
"""
# 소수(prime number) : 1과 자기 자신으로만 나누어지는 정수
# 2부터 10까지의 정수들 중에서 소수를 찾아서 출력

sosu = []
for i in range(2, 11):
    for j in range(2, i):
        x = i%j
        if x==0:
            break
        else:
            continue


# 소수(prime number): 1과 자기자신으로만 나누어지는 정수
# 2부터 10까지의 정수들 중에서 소수를 찾아서 출력
for n in range(2, 11):
    isPrime = True
    for divider in range(2, n):
        if n % divider == 0:
            print(f'{n} = {divider} x {n / divider}')
            isPrime = False
            break
    if isPrime:
        print(f'{n}은 소수!')


# for/while 반복문과 else가 함께 사용되는 경우,
# 반복문이 break 또는 continue를 만나지 않고 범위 전체를 반복했을 때
# else 블록이 실행
# 반복문 중간에 break 또는 continue를 만나면 else는 실행되지 않음.
for i in range(5):
    if i == 3:
        break
    print(i, end='')
else:
    print('반복문 종료')
"""

# for-else 구문을 이용한 소수 찾기
for n in range(2, 11):
    for divider in range(2,n):
        if n% divider == 0: # 약수가 존재 -> 소수가 아님.
            break
    else: # break를 만나지 않았을 때 -> 소수.
        print(f'{n}은 소수:')




