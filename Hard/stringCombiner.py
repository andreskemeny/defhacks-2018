from operator import add

def StringCombiner():
    a = input("Enter a string ")
    b = input("Enter another string ")

    string = ""
    string = string.join(map(add, a, b))
    print(string)

if __name__ == '__main__':
    StringCombiner()
