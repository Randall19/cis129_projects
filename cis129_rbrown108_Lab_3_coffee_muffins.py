""" This program demonstrates interacting with the user
using the input built-in function, calculating a
coffee shop order with associated price information,
calculate a bill subtotal, add tax, and display
a final bill to the customer.

cis129 for Brittany Griwzow author Randall Brown"""
# define default values for number of menu items and tax rate.
coffeeNum=0
muffinNum=0
chocChipNum=0
brownieNum=0
taxRate=.060
# request customer name, display menu
customerName= input("PLease provide your name for your order today. ")
print("Welcome, ", customerName, ", We have four items on our menu today, all American favorites: \n\n" , "Coffee at $5.00 per cup \n", "Muffin at $4.00 Each \n", "Chocolate Chip Cookies at $2.00 each \n", "Brownies at $3.00 each \n")
# begin order process with muffins
muffinAnswer =(input("Would you like to order any Muffins today? \nPlease enter Y for yes or N for No \n"))
if muffinAnswer == "Y":
    muffinNum = int(input("How many Muffins would you like to order?  \n "))
elif muffinAnswer == "N":
    print("you have declined the Muffin option. \n")
# continue order process with coffee
coffeeAnswer=input("Would you like to order any coffees today? \nPlease enter Y for yes or N for No \n")
if coffeeAnswer == "Y":
    coffeeNum = int(input("How many coffees would you like to order today? \n"))
elif coffeeAnswer == 'N':
    print("you have declined Coffee option. \n")
chocChipAns=input("Would you like to order any chocolate chip cookies today? \nPlease enter Y for yes or N for No \n")
if chocChipAns== "Y":
    chocChipNum = int(input("How many chocolate chip cookies would you like to order today? \n"))
elif chocChipAns == "N":
     print("you have declined the chocolate chip cookies option. \n")
brownieAns=input("Would you like to order any brownies today? \nPlease enter Y for yes or N for No \n")
if brownieAns== "Y":
    brownieNum = int(input("How many brownies would you like to order today? \n"))
elif brownieAns == "N":
     print("you have declined the brownies option. \n")
# calculate bill
coffeeBill = coffeeNum * 5
muffinBill = muffinNum * 4
chocChipBill = chocChipNum * 2.00
brownieBill = brownieNum * 3.00
subtotal = muffinBill + coffeeBill + chocChipBill + brownieBill
tax = subtotal * taxRate
total = subtotal + tax
# summarize and display bill
print('************************************')
print("My Coffee and Muffin Shop")
print('Number of coffees bought?')
print(coffeeNum)
print('Number of muffins bought?')
print(muffinNum)
print('Number of Chocolate Chip Cookies bought?')
print(chocChipNum)
print('Number of Brownies bought?')
print(brownieNum)
print('************************************')
print()
print('************************************')
print('My Coffee and Muffin Shop Receipt')
print(coffeeNum, ' Coffee at $5 each: $ ', coffeeBill)
print(muffinNum, 'Muffins at $4 each: $ ', muffinBill)
print(chocChipNum, 'CC Cookiess at $2 each: $ ', chocChipBill)
print(brownieNum, 'Brownies at $3 each: $ ', brownieBill)
print('6% tax: ', tax)
print('_______________________________________')
print('Total: $ ', total)
print('************************************')
      
if total >0:
    print("Thank you ", customerName, ", for your order for ", muffinNum, " Muffins and ", coffeeNum, " Coffees  \n", chocChipNum, "Chocolate Chip Cookies ",  brownieNum, "Brownies \n", "The total bill including tax is : $", total)
    print('your order will be ready momentarily')
else:
    print(customerName, " You have decided not to order today.  Please come back tomorrow for the new menu addition, \'DONUTS\'")
         
        
    
