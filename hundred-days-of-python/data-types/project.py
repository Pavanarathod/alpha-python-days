def your_life_span():
    age = int(input("Enter you age and i'll tell how day you left ? : "))
    year = 365
    weeks = 52
    months = 12

    years_remaining = 90 - age
    days_remaining = years_remaining * year
    weeks_remaining =  years_remaining * weeks 
    months_remaining = years_remaining * months

    return f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months"

print(your_life_span())
