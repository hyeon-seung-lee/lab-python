"""
클래스(class):
프로그램에서 만들려고 하는 대상(객체)이 가져야 할
속성(데이터)과 기능(함수)을 묶어서 하나의 데이터타입으로 설계한 것.

메소드(method): 클래스가 가지고 있는 함수
필드(field): 클레스가 가지고 있는 데이터(변수)
"""


# TV 소프트웨어 작성
# TV 속성(데이터): 채널, 음량, 전원
# TV 기능: 채널 변경, 음량 변경, 전원 on/off

class BasicTv:
    """
    BasicTv 클래스
    """
    max_channel, min_channel = 15, 1
    max_volume, min_volume = 5, 1

    # init 함수 : 생성자가 호출됐을 때 자동으로 실행되는 메소드(함수)

    def __init__(self, power, channel, volume):
        print('BasicTv 생성자 호출')
        self.power = power
        self.channel = channel
        self.volume = volume

    # 클래스 내부에서 정의하는 함수 : 메소드
    def power_on_off(self):
        if self.power:  # power가 True이면(TV가 켜져 있으면)
            self.power = False
            print('TV를 끕니다.')
        else:  # TV가 꺼져 있으면
            self.power = True
            print('TV를 켭니다.')

    def channel_up(self):
        if self.power:
            if self.channel < self.max_channel:
                self.channel += 1
            else:
                self.channel = self.min_channel
        else:
            pass
        print(f'채널 Up : {self.channel}')

    def channel_down(self):
        if self.power:
            if self.channel > self.min_channel:
                self.channel -= 1
            else:
                self.channel = self.max_channel
        else:
            pass
        print(f'채널 Down : {self.channel}')

    def volume_up(self):
        if self.power:
            if self.volume < self.max_volume:
                self.volume += 1
            else:
                pass
        else:
            pass
        print('볼륨 Up:', self.volume)

    def volume_down(self):
        if self.power:
            if self.volume > self.min_volume:
                self.volume -= 1
            else:
                pass
        else:
            pass
        print('볼륨 Down:', self.volume)


# 클래스 설계(정의)

if __name__ == '__main__':
    # 클래스의 객체(instance)를 생성해서 변수에 저장
    # 생성자(constructor) 호출, -> 객체(object) 생성
    tv1 = BasicTv(power=False, channel=1, volume=0)

    # 생성자 : BasicTv
    print(tv1)

    tv1.power_on_off()  # 전원 on
    print(f'현재 채널 : {tv1.channel}')

    for _ in range(16):
        tv1.channel_up()
    for _ in range(17):
        tv1.channel_down()
    for _ in range(6):
        tv1.volume_up()
    for _ in range(7
                   ):
        tv1.volume_down()

