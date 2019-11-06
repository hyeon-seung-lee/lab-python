
#13
t = 'T'
for x in range(7):
    print(t*x)

#14
space = ' '
for x in range(7):
    print(space*(7-x)+t*x)
print()
#15
x= 1
while x <= 7:
    print(t * x)
    x+=1
y=1
print()

while y <= 7:
    print(space*(7-y)+t*y)
    y+=1

#16-A
rat_1_weight = 1
rat_2_weight = 1
rat_1_rate = 0.04
rat_2_rate = 0.035
x = 1
while rat_1_weight < 1.25:
    rat_1_weight *= (1+rat_1_rate)
    print(f'{x}주차 : {rat_1_weight}')
    x+=1
print(f'{x}주 걸린다.')

#16-B
rat_1_weight = 1
rat_2_weight = 1
rat_1_rate = 0.04
rat_2_rate = 0.035
x = 1
while rat_1_weight < (1.1*rat_2_weight):
    rat_1_weight *= (1+rat_1_rate)
    rat_2_weight *= (1 + rat_2_rate)
    print(f'{x}주차 rat1 : {rat_1_weight}')
    print(f'{x}주차 rat2 : {rat_2_weight}')
    x+=1
print(f'{x}주 걸린다.')
