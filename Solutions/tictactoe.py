def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    combinationsToWIn = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nINVALID MOVEMENT")
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nINVALID MOVEMENT")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nINVALID MOVEMENT")
                        continue
                except ValueError:
                   print("\nINVALID MOVEMENT")
                   continue

    def board_check():
        count = 0
        for a in combinationsToWIn:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("P1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("P2!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = board_check()
        if end == True:
            break
        print("P1,place an x")
        p1()
        print()
        draw()
        end = board_check()
        if end == True:
            break
        print("P2,place an O")
        p2()
        print()

tic_tac_toe()