def DogAge(humanYears):
    dogYears = 0
    if humanYears <= 2:
        dogYears = humanYears * 10.5
    if humanYears > 2:
        dogYears = ((humanYears - 2) * 4) + 21

    print(dogYears)


if __name__ == '__main__':
    DogAge(15)
