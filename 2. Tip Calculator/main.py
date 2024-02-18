#Tip Calculator
print("Welcome to the Tip Calculator!")

#Get bill total
total = float(input("What was the total of the bill? $"))
total = round(total,2)

#Get the tip amount for the waiter/waitress
tip = int(input("What percentage would you like to give? 10 12 15 18 20?"))
tip = tip / 100
tip *= total

#Splitting evenly get the amount of people
people = int(input("How many people are splitting the bill?"))

#Get final amount and round to nearest penny
final = (total + tip) / people
final = round(final, 2)

#Display each persons share
print(f"Each person should pay ${final}")
