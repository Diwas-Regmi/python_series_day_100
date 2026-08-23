import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()-_=+"
length = random.
password = (
            random.choices(letters, k=8)
            # + random.choices(numbers, k=4)
            # + random.choices(symbols, k=4)
    )
print(password)