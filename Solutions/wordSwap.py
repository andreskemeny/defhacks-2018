def WordSwap():
    string = input("Enter a string ")

    word1, word2 = string.split(" ", 1)
    print(word2, word1)

if __name__ == '__main__':
    WordSwap()