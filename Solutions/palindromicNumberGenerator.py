number= str(input('number'))
reversenumber= number[::-1]
ispalindrome = False
print(reversenumber)

if number == reversenumber:
    print('number already palindromic')
else:
    pass

while not ispalindrome :
    if str(number) != str(number)[::-1]:
        number = (int(number) + (int(str(number)[::-1])))

    else:
        print(number)
        ispalindrome = True
        pass


