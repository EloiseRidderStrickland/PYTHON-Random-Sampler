
# AUTHOR :: Eloise Ridder-Strickland
# PURPOSE :: Collect & Combine Tag elements to process for uniqueness.

import generators
import random
    
"""
    The 'join_tag' function collects the results of the 'generators.py' call
    and joins the letter component to the integer component and returns the string 'tag'.
"""

# === MATCH STRING === (Base Tag)
def join_tag():
    tag = generators.random_letters(3) + str(generators.random_integers())                        # Converts integers into String and combines into a tag.
    return(tag)

"""
    The 'shuffle_list' function takes the base string 'tag' as defined in 'join_tag'
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
