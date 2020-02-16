def DeletingWords():
    word = input("Enter a word ")

    newString = ""
    for x in range(len(word)):
        if x % 3 != 0:
            newString = newString + word[x]

    print(newString)

if __name__ == '__main__':
    DeletingWords()
