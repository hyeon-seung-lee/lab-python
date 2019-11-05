"""
가위(1)/바위(2)/보(3)
"""
import numpy as np

print('가위 바위 보 게임 ')
print('[1] 가위')
print('[2] 바위')
print('[3] 보')
print('-------------------')
user = int(input('선택하세요>> '))

computer = np.random.randint(1,4) # 1 <= com < 4 난수 발생
print(computer)
# 12, 13, 23, 21, 31, 32
if user == 1 and computer == 2:
    print('패배하셨습니다')
elif user == 1 and computer == 3:
    print('승리하셨습니다')
elif user == 2 and computer == 3:
    print('패배하셨습니다')
elif user == 2 and computer == 1:
    print('승리하셨습니다')
elif user == 3 and computer == 1:
    print('패배하셨습니다')
elif user == 3 and computer == 2:
    print('승리하셨습니다')
else:
    print('무승부')

