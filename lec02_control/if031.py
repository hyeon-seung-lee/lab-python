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


result = user-computer
if result == 0 : #비긴 경우
    print('무승부')
elif result == 1 or result == -2 : #user
    print('승리하셨습니다')
else:
    print('패배하셨습니다')
