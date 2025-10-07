
# AUTHOR :: Eloise Ridder-Strickland
# PURPOSE :: Generate a random Alpha-numeric six digit string.

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
    
# === MATCH STRING === (Base Tag)
def join_tag():
    tag = random_letters(3) + str(random_integers())                        # Converts integers into String and combines into a tag.
    return(tag)

# === SHUFFLED STRING LIST === (Selection Match Case)
def shuffle_list(base_tag):
    # Splits into base components
    letters = base_tag[:3]                                                  # Last 3 characters (the letters)
    numbers = base_tag[3:]                                                  # First 3 characters (the digits)
    
    # Convert to lists for shuffling
    letter = list(letters)
    number = list(numbers)
    
    # Create 3 unique shuffled combinations
    shuffled_tags = []
    for i in range(3):
        # Copies
        shuffled_letters = letter.copy()
        shuffled_numbers = number.copy()
        
        # Shuffle sequences
        random.shuffle(shuffled_letters)
        random.shuffle(shuffled_numbers)
        
        # Combine & Join into string.
        match_tag = ''.join(shuffled_letters + shuffled_numbers)
        shuffled_tags.append(match_tag)
    
    return shuffled_tags
        


