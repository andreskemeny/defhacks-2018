
X = int(input())
if X > 1:
    for i in range(2, X):
        if (X % i) == 0:
            print("FALSE")
            break
    else:
        print('TRUE')

else:
    print('FALSE')