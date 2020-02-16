import math

def PerfectSquare():
    x = int(input('first number '))
    y = int(input('second number '))

    lst = list(range(x, y))
    output = []


    if x < y:
        lst = list(range(x, y))
    if x > y:
        lst = list(range(y, x))

    lst = list(range(10, 50))
    for n in lst:
        if math.sqrt(n).is_integer():
            output.append(n)


    print(str(output).strip("[]"))


if __name__ == '__main__':
    PerfectSquare()
