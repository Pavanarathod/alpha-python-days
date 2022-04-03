print("Welcome to Python Pizza Deliveries.")

size = str(input("What size pizza do you want? S, M OR L: "))
add_pepperoni = str(input("Do you want pepperoni? Y or N: "))
extra_cheese = str(input("Do you want extra cheese: Y or N: "))

total_bill = 0

if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
else:
    total_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3


if extra_cheese == "Y":
    total_bill += 1


print(f"you final bill is ${total_bill}")