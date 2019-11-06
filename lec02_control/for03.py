"""
for-in 구문 연습
"""
"""
# 구구단 2단부터 9단까지 출력

for i in range(2,10):
    print(i,'단')
    for j in range(1,10):
        print(f'{i}*{j}={i*j}')
    print()

# 구구단 2단은 2*2, 3단은 3*3 ... 9단은 9*9 까지
for i in range(2, 10):
    print(i, '단')
    for j in range(1, i+1):
        print(f'{i}*{j}={i*j}')
    print()

#
for i in range(2,10):
    print(i,'단')
    for j in range(1,10):
        print(f'{i}*{j}={i*j}')
        if i == j:
            break
    print()
"""
for i in range(1,10):
    if i == 5:
        break
    print(i, end=' ')
print()

for i in range(1,10):
    if i == 5:
        continue
    print(i, end=' ')
print()