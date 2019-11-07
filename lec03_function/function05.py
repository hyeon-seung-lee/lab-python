"""
가변 길이 인수(variable-length argument)
함수를 호출할 때 전달하는 argument의 갯수가 다양하게 변하는 것
"""
"""
print()


def fn_vararg(*varargs):
    print(*varargs)
    for arg in varargs:
        print(arg)

fn_vararg(1, 2, 3, 4)
"""


#
#
# def summation(*args):
#     """
#     임의의 갯수의 숫자들을 전달받아서 그 숫자들의 총합을 리턴하는 함수
#
#     :param args: 합계를 계산할 숫자들(갯수 제한 없음)
#     :return: 숫자들의 합
#     """
#     f_sum = 0
#     for number in args:
#         f_sum += number
#     return f_sum
#
#
# print(summation(1, 2, 3, 4, 5))
#
#
# def fn_vararg2(a, *b):
#     print(f'a = {a}')
#     print(f'b = {b}')
#
# # fn_vararg2() # a 값을 전달하지 않으면 에러 발생
# fn_vararg2(1) # b는 가변길이 파라미터이므로 인수를 전달하지 않아도 됨
#
#
# def fn_vararg3(*a, b):
#     print(f'a = {a}')
#     print(f'b = {b}')
#
#
# # fn_vararg3() # b 파라미터의 argument가 없으므로 에러
# # fn_vararg3(1) # TypeError: fn_vararg3() missing 1 required keyword-only argument: 'b'  >> ??
# # fn_vararg3(1, 2) # TypeError: fn_vararg3() missing 1 required keyword-only argument: 'b'  >> ??
# fn_vararg3(1, b= 2) # 출력 성공. keyword-only 는 반드시 b라고 지정해주어야 한다는 뜻


def calculator(*values, operator):
    """
    operator가 '+'인 경우에는 values들의 합계를 리턴하고,
    operator가 '*'인 경우에는 values들의 곱을 리턴하는 함수
    :param values: ','로 구분한 계산할 숫자들을 나열
    :param operator: '+' or '*'를 넣어준다(따옴표 필수)
    :return: int 계산 결과값
    """

    if operator == '+':
        add_result = 0
        for x in values:
            add_result += x
        return add_result

    elif operator == '*':
        multiple_result = 1
        for x in values:
            multiple_result *= x
        return multiple_result
    else:
        print("+ 또는 *만 입력하세요.")


print(calculator(1, 2, 3, 4, operator='-'))
print(calculator(1, 2, 3, 4, operator='*'))
