"""
1) emp 테이블에서 부서번호를 입력 받아서 해당 부서의 사번, 이름, 부서번호 출력
2) emp 테이블에서 이름을 입력 받아서, 해당 글자가 포함된 직원들의 사번, 이름, 급여를 출력
"""

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호 입력>> '))
        sql1 = 'select empno, ename, deptno from emp where deptno = :p_deptno'
        cursor.execute(sql1, p_deptno=deptno)
        connection.commit()
        for row in cursor:
            print(row)

print('====================================')
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        ename = '%'+input('사원 이름을 입력>> ')+'%'
        sql2 = "select empno, ename, sal from emp where ename like upper(:p_ename)"
        cursor.execute(sql2, p_ename=ename)
        for empno, ename, sal in cursor:
            print(empno, ename, sal)
