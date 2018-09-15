import datetime
td = open("TaskList.txt", "w+")
name = str(input("enter user's name: "))
greeting = 'Hello' + " " + name
print(greeting.format(name))
tday = datetime.date.today()
weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dayDate = tday.strftime("{%w} %Y-%m-%d").format(*weekday)
print('\n' + "Its" + ' ' + dayDate + '\n')
td.write('line ' + '\t' + 'Task Title ' + '\t' + 'Priority' + '\t' + 'Status' + '\t\t' + 'Day/Date' + '\n')
positiveChoice = ['yes', 'y']
negativeChoice = ['no', 'n']

inputChoice = input("Do you want to enter today's tasks? (y/N) ").lower()
if inputChoice in positiveChoice:
    for i in range(5):
        if (i == 0):
            td.write('T1' + '\t\t' + input("enter your first task: ") + '\t\t\t' + input(
                "enter a number between 1 to 5: ") + '\t\t' + 'Pending' + '\t\t' + dayDate + '\n')
        elif (i == 1):
            td.write('T2' + '\t\t' + input("enter your second task: ") + '\t\t\t' + input(
                "enter a number between 1 to 5: ") + '\t\t' + 'Pending' + '\t\t' + dayDate + '\n')
        elif (i == 2):
            td.write('T3' + '\t\t' + input("enter your third task: ") + '\t\t\t' + input(
                'enter a number between 1 to 5: ') + '\t\t' + 'Pending' + '\t\t' + dayDate + '\n')
        elif (i == 3):
            td.write('T4' + '\t\t' + input("enter your fourth task: ") + '\t\t\t' + input(
                "enter a number between 1 to 5: ") + '\t\t' + 'Pending' + '\t\t' + dayDate + '\n')
        else:
            td.write('T5' + '\t\t' + input("enter your last task of the list: ") + '\t\t\t' + input(
                "enter a number between 1 to 5: ") + '\t\t' + 'Pending' + '\t\t' + dayDate)

elif inputChoice in negativeChoice:
        print('Have a nice day {0}!!'.format(name) + '!!')

