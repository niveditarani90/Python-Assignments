year = int(input("year of birth"))
if (year % 12 == 0):
    print("monkey")
elif (year % 12 == 1):
    print("rooster")
if (year % 12 == 2):
    print("dog")
elif (year % 12 == 3):
    print("pig")
if (year % 12 == 4):
    print("rat")
elif (year % 12 == 5):
    print("ox")
else:
    print("animal")
