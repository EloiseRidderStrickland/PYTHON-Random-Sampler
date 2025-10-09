
# AUTHOR :: Eloise Ridder-Strickland
# PURPOSE :: Generate a random Alpha-numeric six digit string.

import random
import string

# Test
def main():
    original = join_tag()
    shuffled = shuffle_list(original)
    print(f"\n Match: {original}")
    print("\n Options")
    for index, item in enumerate(shuffled, start=1):
        print(f"{index}. {item}")

# === RANDOM LETTER SEQUENCE GENERATOR ===
def random_letters(length):                                                 # Character Component (Uppercase only)
    char = string.ascii_uppercase                                           # ASCII Character Map
    char_comp = ''.join(random.choice(char) for i in range(length))         # Takes the result and joins them into a string.
    return(char_comp)

# === RANDOM NUMBER SEQUENCE GENERATOR ===
def random_integers():                                                       
    integer_comp = random.randint(100, 999)                                 # Generates a random 3 digit number.
    return(integer_comp)

# --------------------------------------------------
    
# === MATCH STRING === (Base Tag)
def join_tag():
    tag = random_letters(3) + str(random_integers())                        # Converts integers into String and combines into a tag.
    return(tag)

"""
    the 'shuffle_list' function takes the base string 'tag' as defined in 'join_tag'
    and seperates the distinct values into there respective halves retaining the first character.
"""

# === SHUFFLED STRING LIST === (Selection Match Case)
def shuffle_list(base_tag):
    # Splits into base components
    letters = base_tag[:3]                                                  # First 3 characters (the letters).
    numbers = base_tag[3:]                                                  # Remaining characters (the digits).
    
    # Separate first letter from the rest
    first_letter = letters[0]                                               # Keep first letter fixed.
    remaining_letters = letters[1:]                                         # Letters to shuffle.
    
    # Convert to lists for shuffling
    letter = list(remaining_letters)                                        # Converts letters to a list.
    number = list(numbers)                                                  # Converts numbers.

    shuffled_tags = set()                                                   # Using a 'set' for uniqueness.
    max_attempts = 25                                                       # Prevents the program from inifinitly looping when no unique combiantions are found,
    attempts = 0

    # Create 3 unique shuffled combinations
    while len(shuffled_tags) < 3 and attempts < max_attempts:                                                      # Creates three unique combinations.
        # Copy
        shuffled_letters = letter.copy()
        shuffled_numbers = number.copy()
        
        # Shuffle sequences
        random.shuffle(shuffled_letters)
        random.shuffle(shuffled_numbers)
        
        # Combine
        match_tag = first_letter + ''.join(shuffled_letters) + ''.join(shuffled_numbers)
        shuffled_tags.add(match_tag)

        # Add unique check here.
    if match_tag != base_tag != join_tag:
        shuffled_tags.add(match_tag)

        attempts += 1
    
    return list(shuffled_tags)

# Test     
if __name__ == "__main__":
    main()

