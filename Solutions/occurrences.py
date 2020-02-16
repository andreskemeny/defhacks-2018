wordlist=list(input('word'))
a = wordlist.index('f')
b = len(wordlist) - 1 - wordlist[::-1].index('f')
if a != b:
    print(a, ',', b)
else:
    print(a)

