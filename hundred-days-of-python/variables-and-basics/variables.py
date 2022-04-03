from fint_me import full_name

first_name = str(input("Enter you first name: "))
last_name = str(input("Enter you last name: "))

full_user_name = full_name(first_name, last_name)
print(full_user_name)
print("length fo the user name: ", len(full_user_name))
