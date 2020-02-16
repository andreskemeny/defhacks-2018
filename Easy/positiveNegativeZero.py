def PositiveNegativeZero():
    _in = int(input("Enter a number "))

    if _in > 0:
        print("Positive")
    if _in == 0:
        print("Zero")
    if _in < 0:
        print("Negative")

if __name__ == '__main__':
    PositiveNegativeZero()