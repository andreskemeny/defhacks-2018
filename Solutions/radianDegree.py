import math

def RadianDegree():
    radian = float(input("Enter a radian "))

    degrees = 180 * radian / math.pi
    print(degrees)

if __name__ == '__main__':
    RadianDegree()