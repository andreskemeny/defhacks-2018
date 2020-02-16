def isPerfect():
    n = int(input("Enter a number "))

    addition = 0

    listRange = list(range(1,n+1))
    divisorList = []

    # Create a list that consists of the divisors
    for number in listRange:
        if n % number == 0:
            divisorList.append(number)
    divisorList = divisorList[:-1]

    # Add the components of the given list
    for i in divisorList:
        addition = addition + i
    if (addition == n):
        print(n, "is perfect.")
    else:
        print(n, "is not perfect.")


if __name__ == '__main__':
    isPerfect()