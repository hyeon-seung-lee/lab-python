from math import sqrt

distance = int(input('이동 거리?: '))
n = int((sqrt(1 + 4 * distance) - 1) / 2)+1
# n = int(distance/2)
print('n: ',n)
num_of_moves = []
for i in range(n):
    for j in range(i + 1):
        x = 2 * (i + 1) - 1
        print(x, end=' ')
        num_of_moves.append(x)
    for j in range(i + 1):
        y = 2 * (i + 1)
        print(y, end=' ')
        num_of_moves.append(y)
print('\n')
print("distance: ", num_of_moves[distance])