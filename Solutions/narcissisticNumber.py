def isNarcissistic():
    n = int(input("Pick a number "))

    digits = []
    result = 0

    digits = [int(d) for d in str(n)]

    # Every component of the list is elevated to the number of digits the number has
    for digit in digits:
        # The number is elevated
        digit = (digit ** len(digits))
        result = result + digit

    if (result == n):
        print(n, "is narcissistic")
    else:
        print(n, "is not narcissistic")

if __name__ == '__main__':
    isNarcissistic()