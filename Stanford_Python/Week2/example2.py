money = int(input("plz enter money in cents"))
Q = money // 25 # number of quarters
money = money % 25 # amount of money left after taking out the quarteres
D = money // 10 # the number of dimes
money = money % 10
N = money // 5 # the number of nickles
P = money % 5 # the number of pennies
print("Quarters="+str(Q)+"\n"+"Dimes="+str(D)+"\n"+
      "Nickles="+str(N)+"\n"+"Pennies="+str(P))

