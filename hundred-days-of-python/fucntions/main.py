import function_days
import art

def calculate_data():
    height = int(input('Enter the height of the wall ?: '))
    width = int(input('Enter the width of the wall ?: '))
    cover = int(input('Enter the cover of the wall ?: '))
    result = function_days.paint_cals(height, width, cover)
    return print(f"you'll need {result} cans of result.") 


def encode_text():
    print(art.logo)
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if(direction == "encode"):
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
            print(f"You'r encrypted text is {function_days.encrypt(text, shift)}") 
        if(direction == "decode"):
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
            print(f"You'r encrypted text is {function_days.decrypt(text, shift)}")
        continue_decode = str(input("Type 'YES' if you want to continue or 'NO'")).lower()
        if continue_decode == "no":
            print("Good bye...") 
            should_continue = False

# function_days.find_prime_number(73)
# calculate_data()
encode_text()