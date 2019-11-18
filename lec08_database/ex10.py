"""
emp, dept 테이블에서
부서 번호를 입력 받아서
해당 부서 직원의 사번, 이름, 급여, 부서 번호, 부서 이름
"""

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('부서 번호 입력>>'))
        sql1 = """select e.empno, e.ename, sal, d.deptno, d.dname
                    from emp e, dept d
                    where d.deptno = :deptno and d.deptno = e.deptno"""
        cursor.execute(sql1, deptno=deptno)
        connection.commit()
        for empno, ename, sal, deptno, dname in cursor:
            print(empno, ename, sal, deptno, dname)
