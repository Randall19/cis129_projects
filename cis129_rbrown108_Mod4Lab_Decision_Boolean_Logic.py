"""This is an exercise to illustrate the use of if, elif statements.
The program will prompt the user to input monthly sales and monthly
sales percent increase and then use those values to print out the calculated
store and employee bonuses if any.
CIS129 for Brittany Griwzow by author Randall Brown rbrown108"""

storeAmount = 0
empAmount = 0
salesIncrease = 0
monthlySales = 0

monthlySales=float(input("Please enter the monthly sales amount as a whole number without commas "))

if monthlySales >= 110000:
	storeAmount = 6000
elif monthlySales >= 100000:
	storeAmount = 5000
elif monthlySales >= 90000:
	storeAmount = 4000
elif monthlySales >= 80000:
	storeAmount = 3000
else:
	storeAmount = 0

salesIncrease=float(input("Please enter the monthly percent increase as a decimal number "))

salesIncrease=salesIncrease/100

if salesIncrease >= .05:
	empAmount = 75
elif salesIncrease >= .04:
	empAmount = 50
elif salesIncrease >= .03:
	empAmount = 40
else:
	empAmount = 0

print("The store bonus amount is $ ", storeAmount)
print("The employee bonus amount is $ ", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
	print("Congrats! You hae reached the highest bonus amounts possible!")


