height = float(input("enter teh height in meter"))
weight = float(input("enter the weight in kg"))
BMI = weight/height**2
print (round((BMI),2))
if(BMI <= 18.5):
    print("underweight")
elif(BMI <= 24.9):
    Print("Normal")
elif(BMI <= 29.9):
    print("Overwieght")
else:
    Print("Obese")


count = 0
while count < 10:
    print("Programming is fun!")
    count = count + 1


