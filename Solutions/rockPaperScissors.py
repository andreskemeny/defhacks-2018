import random
optionslist=['r','p','s']
computerScore = 0
playerScore = 0
play =1
playagain = True
while playagain == True:
    computerChooses = random.choice(optionslist)
    playerChooses = input('chose rock[r], paper[p] scissors[s]')
    if playerChooses == "r" and computerChooses == "p":
        print('computer chose', '', computerChooses)
        print('computer wins')
        computerScore += 1
    elif playerChooses == "p" and computerChooses == "r":
        print('computer chose', '', computerChooses)
        print('player wins')
        playerScore += 1
    elif playerChooses == "r" and computerChooses == "s":
        print('computer chose', '', computerChooses)
        print('player wins')
        playerScore += 1
    elif playerChooses == "s" and computerChooses == "r":
        print('computer chose', '', computerChooses)
        print('computer wins')
        computerScore += 1
    elif playerChooses == "s" and computerChooses == "p":
        print('computer chose', '', computerChooses)
        print('player wins')
        playerScore += 1
    elif playerChooses == "p" and computerChooses == "s":
        print('computer chose', '', computerChooses)
        print('computer wins')
        computerScore += 1
    elif playerChooses == "r" and computerChooses == "r":
        print('computer chose', '', computerChooses)
        print('draw')
    elif playerChooses == "p" and computerChooses == "p":
        print('computer chose', '', computerChooses)
        print('draw')
    elif playerChooses == "s" and computerChooses == "s":
        print('computer chose', '', computerChooses)
        print('draw')
    else:
        print('please choose a valid option')
    print('computerscore: ', computerScore)
    print('playersocre: ', playerScore)
    playagain = input('would you like to play again y/n')
    if playagain.lower() == 'y':
        playagain = True
    else:
        playagain = False

