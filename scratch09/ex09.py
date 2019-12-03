"""
emp.csv 파일을 읽어서, DataFrame을 생성
- 급여(sal)가 2000 이상인 직원들의 [모든 정보]를 출력 (boolean indexing 사용)
- 부서 번호(deptno)가 10번인 직원들의 [모든 정보]를 출력
- 급여가 전체 직원의 급여의 평균보다 많은 직원의 (사번, 이름, 급여)를 출력
-  30번 부서에서 일하는, 직책이 salesman인 직원들의 (사번, 이름, 급여, 부서번호)를  검색해서 출력
- 20, 30번 부서에서 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 (사번, 이름, 급여, 부서번호)를 출력
- 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인 직원들의 [모든 정보]를 검색
- 사원 이름에 'E'가 포함된 직원들의 [이름]을 출력 -> (str.contains())
- DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 실행
"""
import numpy as np
import pandas as pd

emp_table = pd.read_csv('emp.csv', header=None,
                        names=['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno'])
print(emp_table)
# 1- 급여(sal)가 2000 이상인 직원들의 [모든 정보]를 출력 (boolean indexing 사용)
print('1:\n', emp_table[emp_table['sal'] >= 2000])

# 2- 부서 번호(deptno)가 10번인 직원들의 [모든 정보]를 출력
print('2:\n', emp_table[emp_table['deptno'] == 10])
# 3- 급여가 전체 직원의 급여의 평균보다 많은 직원의 (사번, 이름, 급여)를 출력
emp_sal_mean = emp_table['sal'].mean()
print('3:\n', emp_table[emp_table['sal'] > emp_sal_mean][['empno', 'ename', 'sal']])

# 4-  30번 부서에서 일하는, 직책이 salesman인 직원들의 (사번, 이름, 급여, 부서번호)를  검색해서 출력
print('4:\n', emp_table[emp_table['job'] == 'SALESMAN'][['empno', 'ename', 'sal', 'deptno']])
# 5- 20, 30번 부서에서 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 (사번, 이름, 급여, 부서번호)를 출력
dept_cond1 = emp_table['deptno'] == 20
dept_cond2 = emp_table['deptno'] == 30
sal_cond = emp_table['sal'] > 2000
print('5:\n', emp_table[(dept_cond1 | dept_cond2) & sal_cond][['empno', 'ename', 'sal', 'deptno']])
# 6- 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인 직원들의 [모든 정보]를 검색
# print(emp_table[emp_table['comm'].isna])
print('6:\n', )
# emp_nocomm= emp_table['comm']
# print(np.isnan(emp_nocomm[0]))
# print(np.isnan(np.nan))
# emp_table.loc[emp_nocomm.notnull()]
not_comm = np.isnan(emp_table['comm'])
have_mgr = np.invert(np.isnan(emp_table['mgr']))
job_mgr_clerk = (emp_table['job'] == 'MANAGER') | (emp_table['job'] == 'CLERK')
print(emp_table[not_comm & have_mgr & job_mgr_clerk])

# 7- 사원 이름에 'E'가 포함된 직원들의 [이름]을 출력 -> (str.contains())
print('7:\n')
name_e = emp_table['ename'].str.contains(pat='E')
print(emp_table[name_e][['ename']])

# 8- DataFrame을 csv 형식으로 파일에 write하는 함수를 찾아서 실행
print('8:\n')
emp_table.to_csv('emp_csv.csv', encoding='UTF-8')
