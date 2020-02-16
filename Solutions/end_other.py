def EndOther():
    string1 = input("Enter a string ")
    string2 = input("Enter another string ")

    string1 = string1.lower()
    string2 = string2.lower()
    string1len = len(string1)
    string2len = len(string2)

    if string1[-string2len:] == string2:
        print("True")
    if string2[-string1len:] == string1:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    EndOther()