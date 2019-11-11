# 1부터 n까지 숫자들의 합을 리턴하는 함수
numbers = [10, 20, 70, 50, 99, 100, 74, 26, 36, 94, 87, 200]
print(f'numbers : {numbers}')


def my_sum(args):
    total = 0
    for i in args:
        total += i
    return total


print(f'my_sum : {my_sum(numbers)}')


# 1부터 n 가지 숫자들의 제곱합을 리턴하는 함수


"""
def my_square_sum(args):
    total = 0
    for i in args:
        total += i**2
    return total


print(f'my_square_sum:{my_square_sum(numbers)}')

"""

# 숫자들의 리스트를 전달 받아서 최댓값을 찾아서 리턴하는 함수


def my_max(args):
    fst = args[0]
    for i in range(len(args)):
        if fst < args[i]:
            fst = args[i]
        else:
            continue
    return fst




print(f'max:{my_max(numbers)}')
# 숫자들의 리스트를 전달받아서 최댓값의 인덱스를 리턴하는 함수( 중복되면 첫 번째 최댓값의 인덱스 )
# sorted(list): list를 정렬한 새로운 리스트를 리턴, 원본 리스트는 순서가 그대로 유지됨
# list.sort(): 원본 리스트를 정렬해서 순서를 바꿈. 값을 리턴하지 않음.
sorted_values = sorted(numbers, reverse =True)
print(f'sorted_values: {sorted_values}')
numberses = numbers
numberses.sort()
print(f'numberses : {numberses}')


# enumerate 인덱스를 자동으로 증가시켜 줌?
def my_max_index(args):
    fst = args[0]
    index = 0
    for i in range(len(args)):
        if fst < args[i]:
            fst = args[i]
            index = i
        else:
            continue
    return index


print(f'my_max_index: {my_max_index(numbers)}')


# 숫자들의 리스트를 전달받아서 중앙값을 리턴하는 함수
def my_middle_arg(args):
    for j in range(len(args)):
        for i in range(j, len(args)-1):
            if args[i] > args[i+1]:
                arg1 = args[i+1]
                args[i+1] = args[i]
                args[i] = arg1
            else:
                continue
    n = len(args)
    if len(args) % 2 == 0:
        moa = (args[n//2]+args[n//2-1])/2             # index이므로 길이/2의 '몫'과 '몫 -1' 이 되어야 한다.
    else:
        moa = args[n//2]

    print(f'args : {args}')
    print(f'middle of args : {moa}')


my_middle_arg(numbers)