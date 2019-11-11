def user_input():
    """
    사용자에게 1, 2, 3 중 하나의 숫자를 입력하도록 안내.
    사용자가 입력한 숫자를 리턴
    사용자가 숫자로 변환할 수 없는 문자를 입력하면, 안내문 출력 후 다시 입력 받음.
    사용자가 1, 2, 3 이외의 숫자를 입력하면, 안내문 출력 후 다시 입력 받음.
    :return: 1, 2, 3 중의 하나를 리턴
    """
    while True:
        try:
            numbers = int(input('1, 2, 3 중 하나의 숫자를 입력 : '))
            if numbers > 3 or numbers < 1:
                raise ValueError('1111')
            print(f'입력한 숫자 : {numbers}')
            return numbers

        except ValueError as e:
            print('숫자를 입력하세요')

x = user_input()
print(f"user_input():{x}")
