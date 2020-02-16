from math import sqrt

def Pythagorean():
    a = int(input('Length of side a '))
    b = int(input('Length of side b '))

    side_c = sqrt(a * a + b * b)

    print('The length of side c is ')
    print(side_c)


if __name__ == '__main__':
    Pythagorean()