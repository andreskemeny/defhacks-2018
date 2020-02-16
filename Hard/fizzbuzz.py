def fizzbuzz():
    x = int(input("Starting number "))
    y = int(input("Ending number "))
    output = ""
    count = 0
    for number in range(x, y):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")

        else:
            count = count + 1

    print(output)
    print(count)

if __name__ == '__main__':
    fizzbuzz()
