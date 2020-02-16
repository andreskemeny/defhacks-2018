def isHarshad():
    n = int(input("Enter a number "))

    digits = []
    result = 0

    digits = [int(d) for d in str(n)]

    for digit in digits:
        result = result + digit

    if (n % result == 0):
        print(n, "is harshad")
    else:
        print(n, "is not harshad")

if __name__ == '__main__':
    isHarshad()
