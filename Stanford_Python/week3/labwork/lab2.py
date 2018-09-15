year = int(input("enter the year: "))
if(year % 4 == 0 and year%100 != 0) or (year%400 == 0):
    print("The year {0} is leap year".format(year))
else:
    print("The year {0} is not leap year".format(year))
