# Write a program that randomly generates an
# integer between 0 and 100, inclusive. The
# program prompts the user to enter a number
# continuously until the number matches the
# randomly generated number. For each user
# input, the program tells the user whether the
# input is too low or too high, so the user can
# choose the next input intelligently.#



import random
target = random.randint(0,50)
guess_number = int(input("enter a number between 0 and 100: "))
while guess_number != target:
    if (guess_number < target):
        guess_number = int(input("enter a larger number"))
    else:
        guess_number = int(input("enter a smaller number"))
print("Congrats!!!")
