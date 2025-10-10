# AUTHOR :: Eloise Ridder-Strickland
# PURPOSE :: Generate a random three integer & letter string combination.

import random
import string

# === RANDOM LETTER SEQUENCE GENERATOR ===
def random_letters(length):                                                 # Character Component (Uppercase only)
    char = string.ascii_uppercase                                           # ASCII Character Map
    char_comp = ''.join(random.choice(char) for i in range(length))         # Takes the result and joins them into a string.
    return(char_comp)

# === RANDOM NUMBER SEQUENCE GENERATOR ===
def random_integers():                                                       
    integer_comp = random.randint(100, 999)                                 # Generates a random 3 digit number.
    return(integer_comp)