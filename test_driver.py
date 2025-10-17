
# Author :: Eloise Ridder-Strickland
# PURPOSE :: Text Based Interface Logic.
import tag_generation
import random

def option_1():
    print("\n Test Set 1.")

# Pulls the 'base_tag' and 'shuffled_list'.
    original = tag_generation.join_tag()
    shuffled = tag_generation.shuffle_list(original)

# Inserts the 'base_tag' (original) into the list with a random index.
    random_index = random.randint(0, len(shuffled) - 1)
    shuffled.insert(random_index, original)

# Print Results
    print(f"\n Match: {original}")
    print("\n Options")
    for index, item in enumerate(shuffled, start=1):
        print(f"{index}. {item}")

def option_2():
    print("Game 2.")

def option_default():
    print("Please Select From The Menu :)")

# Main Menu (1)
while True:
    print("\n+-------- !TEST INTERFACE --------+")
    print("| Press A number to Enter a Mode  |")
    print("| 1. Tag Generator Game (List)    |") # Select 4, 5, 6 tags to association train.
    print("| 2. Test Space 2                 |") # Same tag Combination, shuffled each round (Association Training)
    print("| 3. Test Space 3                 |") # Training mode, highlights the correct tag in Green for (Association Training).
    print("| 3. Exit                         |")
    print("+---------------------------------+")
    choice = input("Start: ")
# ------------------------------------------------

    if choice == '1':
        option_1()
    elif choice == '2':
        option_2()
    elif choice == '3':
        print("Thanks For Playing! :)")
        break
    else:
        option_default()

        # Standard Identification Game
        # Tag Shuffle
        # Association Trainer