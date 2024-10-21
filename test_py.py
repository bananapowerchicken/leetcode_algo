### --medium--

# caesar cipher
# Write a function that implements the Caesar cipher encryption.
# The function should take a string and a shift value, 
# then return the encrypted version of the string by shifting
#  the letters of the alphabet. For example:
# caesar_cipher('hello', 3)  # Output: 'khoor'
# caesar_cipher('xyz', 2)    # Output: 'zab'

# import string # to get prepared ascii alphabet string


# ALPHABET = string.ascii_lowercase


# def caesar_cipher(input: str, shift: int) -> str:
#     input = input.lower()
#     output = ''
#     for s in input:
#         index_old = ALPHABET.index(s)
#         index_new = index_old + shift
#         if index_new > len(ALPHABET) - 1:
#             index_new = index_new % len(ALPHABET)

#         output += ALPHABET[index_new]
    
#     return output

# # caesar_cipher('hello', 3)
# caesar_cipher('xyz', 2) 

# # edges
# # non chars: 1, ' ', '-' - what to do? i would remove them or make a strict requirements for input
# # or leave them unchanged
# # negative shift check or add such a functionality
# # check if shift is int - otherwise raise an exception
# # zero shift - return input - no extra moves



from enum import Enum, auto

class DiscountType(Enum):
    STANDARD = auto() # any weight - 6%
    SEASONAL = auto() # any weight - 12%
    WEIGHT = auto() # weight <= 10 - 6%, weight > 10 - 18%

def get_discounted_price(cart_weight, total_price, discount_type) -> float:
    if discount_type == DiscountType.STANDART:
        return 0.94 * total_price
    if discount_type == DiscountType.SEASONAL:
        return 0.88 * total_price
    if discount_type == DiscountType.WEIGHT:
        if cart_weight <= 10:
            return 0.94 * total_price
        else:
            return 0.82 * total_price

print(get_discounted_price(12, 100, DiscountType.WEIGHT))