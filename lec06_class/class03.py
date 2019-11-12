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

    def emp_info(self):
        return (f'Employee Number : {self.empno} \n'
                f'Employee Name : {self.ename} \n'
                f'Salary : {self.salary} \n'
                f'Department Number : {self.deptno}')


employee1 = Employee(123, 'hslee', 30000, 100)
print(f'Raised_salary : {employee1.raise_salary(0.3)}')
print(employee1.emp_info())


x = (10, 20)
print(x[1])