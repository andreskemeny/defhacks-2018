def LettersDigits():
    string = str(input("Enter a string "))
    string = list(string)
    letters = 0
    digits = 0
    for x in string:
        if x.isdigit() == True:
            digits = digits + 1
        else:
            letters = letters + 1

    print("Letters" + " " + str(letters))
    print("Digits" + " " + str(digits))


if __name__ == '__main__':
    LettersDigits()
