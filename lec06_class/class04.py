from math import sqrt
"""
클래스 작성, 테스트
"""


class Point:
    """
    2차원(x-y) 평면 상의 점 1개를 저장할 수 있는 클래스
    """

    def __init__(self, x: int, y: int):
        self.point = (x, y)

    def print_point(self):
        """
        Point 객체가 가지고 있는 점의 좌표를 (x, y) 형식으로 출력
        :return: None
        """
        return self.point

    def distance(self, other):
        """
        두 점 사이의 거리를 계산해서 리턴하는 함수
        :param other: 다른 Point 객체
        :return: 두 점 사이의 거리
        """
        distance = sqrt((self.point[0] - other.point[0])**2 + (self.point[1] - other.point[1])**2)
        print(self.point,'와 ', other.point, '의 거리는?')
        return distance


p1 = Point(3, 10)
p2 = Point(7, 100)
print(p1.print_point())
print(p1.distance(p2))

