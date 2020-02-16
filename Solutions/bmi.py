def BMI():
    kg = float(input("Enter a weight in KG "))
    m = float(input("Enter a height in M "))

    print(kg / (m ** 2))

if __name__ == '__main__':
    BMI()