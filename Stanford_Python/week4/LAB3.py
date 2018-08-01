# Write a program which inputs a number and
# determines whether it’s prime or not.
# An integer greater than 1 is prime if its only
# positive divisor is 1 or itself.

#write using if and for loop


n = int(input("enter a number: "))
flag = 0
for i in range(2, n):
    if n % i == 0:
        flag =1
if flag == 0:
    print("its prime!")
else:
    print("Not prime!!")
