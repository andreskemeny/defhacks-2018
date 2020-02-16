def CharInput():
    name = input("Enter your name ")
    age = int(input("Enter your age "))

    year = 2018 - age + 100

    print("Your name is " + name + ". " + "You will turn 100 years old in the year " + str(year))

if __name__ == '__main__':
    CharInput()