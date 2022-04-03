def tip_calculator():
    bill = int(input('What is the total of the bill: '))
    tip = int(input("Tip value: "))
    persons = int(input("How many people to split up the bill: "))
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill * total_tip_amount
    bill_per_person = total_bill / persons

    final_amount = round(bill_per_person, 2)

    return f"Each person should pay: ${final_amount}"

output = tip_calculator()
print(output)