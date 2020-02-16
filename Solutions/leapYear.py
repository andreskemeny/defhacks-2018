import calendar

def IsLeap():
    year = int(input("Enter a year "))

    if calendar.isleap(year) == True:
        print("Leap")
    if calendar.isleap(year) == False:
        print("Common")



if __name__ == '__main__':
    IsLeap()