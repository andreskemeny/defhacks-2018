def Apples():
    n = int(input("Students "))
    k = int(input("Apples "))

    perStudent = k // n
    remaining = k % n

    print(perStudent)
    print(remaining)

if __name__ == '__main__':
    Apples()
