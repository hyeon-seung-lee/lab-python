from math import pi


class Circle:
    # field: 반지름(radius)
    # method:
    #       __init__() : 초기화(객체 생성)함수,
    #       area() : 원에 넓이를 리턴
    # perimeter(): 원의 둘레 길이를 리턴하는 함수
    # __str__() : Circle(r = 12) 형식으로 출력되도록 하기
    # __eq__(): 반지름이 같으면 equal(True)
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise TypeError('radius는 반드시 숫자 타입')

    def area(self):
        return self.radius ** 2 * pi

    def perimeter(self):
        return 4 * pi * self.radius

    def __eq__(self, other): # == 연산자 사용시 호출되는 메소드
        return self.radius == other.radius

    def __str__(self):  # print 사용시 호출되는 메소드
        return f'Circle(r = {self.radius})'

    def __gt__(self, other):
        # greater than: > 연산자를 사용하면 자동으로 호출되는 메소드
        return self.radius > other.radius

    def __ge__(self, other): # greater than or equal to, >= 연산자 사용시 자동 호출
        return self.__gt__(other) or self.__eq__(other)
    #   return self.radius >= other.radius

    def __repr__(self):
        return f'원({self.radius})'

if __name__ == '__main__':
    c1 = Circle(10)
    c2 = Circle(10)
    print(f'area : {c1.area()}')
    print(f'area : {c1.area}')
    print(f'perimeter : {c1.perimeter()}')
    print(f'perimeter : {c1.perimeter}')
    print(c1 == c2)        # __eq__ 함수 실행
    print(c1)
    print(c1>c2)
    print(c1 >= c2)
    print(c1 < c2) # lt 메소드를 지정하지 않아도 gt 의 반대값으로 계산됨

circles = [
    Circle(10),
    Circle(7),
    Circle(100),
    Circle(50),
    Circle(0)
]

print(circles)
print(sorted(circles))
print(sorted(circles, reverse=True))

