"""
클래스 작성, 객체 생성, 메소드 사용 연습
"""


class Employee:
    """
    field: empno, ename, salary, deptno
    method : raise_salary(self, pct)
    """

    def __init__(self, empno, ename, salary, deptno):
        self.empno = empno
        self.ename = ename
        self.salary = salary
        self.deptno = deptno

    def raise_salary(self, pct: int) -> int:
        """
        salary 인상율인 pct 값을 삽입하면
        인상된 연봉 salary를 return 하는 함수
        :param pct: int
        :return:  int
        """
        self.salary = self.salary * (1 + pct)
        return self.salary

    def __repr__(self):
        return (f'(Employee Number : {self.empno} \n'
                f'Employee Name : {self.ename} \n'
                f'Salary : {self.salary} \n'
                f'Department Number : {self.deptno})')


scott = Employee(123, 'hslee', 30000, 100)
# print(f'Raised_salary : {scott.raise_salary(0.3)}')
# print(scott.__repr__())
gil_dong = Employee(500, 'honggildong', 10000, 20)

x = (10, 20)


ohssam = Employee(1012, '오쌤', 500, 30)

employees = [ohssam, gil_dong, scott ]
print(employees)
print()

print(sorted(employees, key = lambda x: x.empno))
print()

print(sorted(employees, key = lambda x: x.salary))