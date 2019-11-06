"""
반복문 연습
"""


# 1+ 2+ 3+ .. 100?

sum_100 = 0
x = 0

while x <= 100:
    sum_100 += x
    x += 1

print(f'sum={sum_100}')

numbers = [x for x in range(1,101)]
print(sum(numbers))

# (1 + 2 + 3 + ... x) <= 100 ?

y = 0
sum1 = 0
sum_arr = []
while y <= 100:
    y += 1
    sum1 += y
    sum_arr.append(sum1)
    print(f'sum_arr[{y-1}] : {sum_arr[y-1]}')
    if sum1<100:
        continue
    else:
        break

print(f'결과값 : sum(1,{y-1}) : {sum_arr[y - 2]}')
print(y-1)



total, z = 0, 1
while total<= 100:
    total += z
    print(f'x = {z}, sum = {total}')
    z += 1
