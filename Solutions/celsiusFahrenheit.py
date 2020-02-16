def CelsiusFahrenheit():
    _in = float(input("Enter a number (celsius) "))

    fahrenheit = 9/5 * _in + 32

    print(fahrenheit)

if __name__ == '__main__':
    CelsiusFahrenheit()