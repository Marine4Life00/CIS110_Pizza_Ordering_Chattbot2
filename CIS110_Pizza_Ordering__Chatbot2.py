print("Hello, my name is Steve your virtual assistant.  I will help you order a pizza!")
print("I am going to ask you a few questions to get your order started.")
userName = input("\nEnter your name: ") 
while len(userName) == 0:
    userName = input("Name can not be blank! Please enter your name: ")
if userName.lower() == "josh emdy":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Let's get that pizza!")

size  = input("\nWhat size pizza do you want?  Enter small, medium, large: :")
while size.lower() not in ["small", "medium", "large"]:
    size = input("Size can not be blank! Please enter small, medium, or large: ")
flavor = input("\nEnter the flavor of pizza: ")
while len(flavor) == 0:
    flavor = input("Flavor can not be blank! Please enter the flavor of pizza: ")
crustType = input("\nWhat type of crust do you want: ")
while len(crustType) == 0:
    crustType = input("Crust type can not be blank! Please enter a flavor:  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value: ")
while not quantity.isdigit():
    quantity = input("\nIs this carry out or delivery: ")
quanty = int(quantity)
method = input("\nIs this carry out or delivery: ")

while method.lower() not in ["carry out", "delivery"]:
    method = input("Invald value! Please enter carry out or delivery: ")
if method.lower() == "delivery":
    deliveryfee = 5
else:
    deliveryFee = 0

    salesTax = 1.1
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
total = (pizzaCost * quanty) * salesTax + deliveryFee

print("-" * 10)
print(f"Thank you {userName} for your order!")
print(f"You ordered {quanty} {size} {flavor} pizza(s) with {crustType} crust cost ${total:,.2f}.")
if total >=50:
    print ("\nCongratulations! You have been awared a $10 off coupon for your next order.")
else:
    print("\nSpend $50 or more to receive a $10 off coupon for your next order.")
    print("-" * 10)

print("Order has been received. ETA 3 mins")
for min in range(3, 0, -1):
    print(min, "minutes remaining")
    for seconds in range(60, 0, -1):
       print(seconds, end="\r")
       import time
       time.sleep(1)
print("Order is ready. Enjoy your pizza!")

keepGoing = input("\nDo you want to place another order? Enter y or n: ")
while keepGoing.lower() not in ["y", "n"]:
    keepGoing = input("Invalid value! Please enter y or n:")