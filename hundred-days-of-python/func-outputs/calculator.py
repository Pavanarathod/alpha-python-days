# Calculator
def add(n1: int, n2: int):
	return n1 + n2

def subtract(n1: int, n2: int):
	return n1 - n2

def multiply(n1: int, n2: int):
	return n1 * n2

def divide(n1: int, n2: int):
	return n1 / n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}


def start(number1: int, number2: int):
	for symbol in operations:
		print(symbol)
	start_calculation = True
	while start_calculation:
		operation_symbol = str(input("Pick on operation from the line above: "))
		calculation_function = operations[operation_symbol]
		first_ans = calculation_function(number1, number2)
		print(f"{number1} {operation_symbol} {number2} = {first_ans}")
		user_option = str(input("Do you want to continue the calculation 'yes' or 'no' "))
		if user_option == 'yes':
			operation_symbol = str(input("Pick you'r second option: "))
			number3 = int(input("Enter the next number: "))
			calculation_function = operations[operation_symbol]
			second_ans = calculation_function(first_ans, number3)
			print(f"{first_ans} {operation_symbol} {number3} = {second_ans}")
		else:
			start_calculation = False

			



