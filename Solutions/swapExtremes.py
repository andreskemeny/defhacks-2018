def SwapExtremes():

    list1 = list(input("Enter a list (separated by spaces) "))
    list2 = list(input("Enter another list (separated by spaces) "))

    list1max = max(list1)
    list1maxpos = list1.index(list1max)

    list2max = max(list2)
    list2maxpos = list2.index(list2max)

    print(list1maxpos)
    print(list2maxpos)

    if list1 != list2:
        newlist1 = list1[list1maxpos] = list2max
        newlist2 = list2[list2maxpos] = list1max
    else:
        pass

    list1[list1maxpos] = list2max
    list2[list2maxpos] = list1max

    print(list1)
    print(list2)

if __name__ == '__main__':
    SwapExtremes()

# [1, 2, 3], [2, 4, 5]