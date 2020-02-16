def ValidNumber():
    _in = input("Enter a number ")

    if _in.isdigit():
        print("Valid Number")
    else:
        print("Invalid Number")

if __name__ == '__main__':
    ValidNumber()