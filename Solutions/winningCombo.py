wordlist =list(input('word'))
counter = 0
revisor = 0
numbreps = 0
length = len(wordlist)

listrep=[]
while counter < length:
    numbreps = wordlist.count(wordlist[counter])
    counter += 1
    listrep.append(numbreps)

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
nicenumb = Remove(listrep)

endLoop=False
for n1 in range(0, len(nicenumb)):
    for n2 in range(1, len(nicenumb)):
        if nicenumb[n1] == nicenumb[n2]:
            endLoop = True
    if endLoop:
        break
if endLoop == False:
    print(max(nicenumb))
else:
    print(min(nicenumb))