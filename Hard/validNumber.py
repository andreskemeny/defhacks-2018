def ValidNumber():
    string = input("Enter a string ")

    for x in string:
        if x.isdigit() is False:
            string = string.replace(x, "")
        else:
            pass

    print(string)


if __name__ == '__main__':
    ValidNumber()