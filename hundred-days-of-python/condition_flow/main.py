def allow_user(customer_height: int):
    if(customer_height > 120):
        return f"Wellcome to wonderlaw'"
    else:
        return f"Sorry, you have to grow taller before you can ride!"

height = int(input("Enter you height: "))

result = allow_user(height)
print(result)