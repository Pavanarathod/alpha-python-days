import math
from turtle import position
def greet():
    print("Hello world!")

def paint_cals(height, width, cover):
    area = height * width
    num_cans = math.ceil(area / width)
    return num_cans

def find_prime_number(number):
    is_prime = True
    for i in range(2, number):
        if(number % i == 0):
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number'")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position +  shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text = letter
    return cipher_text

def decrypt(cipher_text, shift_amount):
    decrypt_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        decrypt_text += alphabet[new_position]

    return decrypt_text
