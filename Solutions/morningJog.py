def MorningJog():
    a = int(input("Enter a number "))
    b = int(input("Enter another number "))

    i = 1
    while a < b:
        a *= 1.1
        i += 1
    print(i, "days")

if __name__ == '__main__':
    MorningJog()