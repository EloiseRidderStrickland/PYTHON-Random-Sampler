
# Author :: Eloise Ridder-Strickland
# PURPOSE :: Text Based Interface Logic.
import random_generators

def option_1():
    print("\n Game 1.")
    
def option_2():
    print("Game 2.")

def option_default():
    print("Please Select From The Menu :)")

# Main Menu (1)
while True:
    print("\n+-------- !TEST INTERFACE --------+")
    print("| Press A number to Enter a Mode  |")
    print("| 1. Identification Game          |") # Select 4, 5, 6 tags to association train.
    print("| 2. Tag Shuffle                  |") # Same tag Combination, shuffled each round (Association Training)
    print("| 3. Association Trainer          |") # Training mode, highlights the correct tag in Green for (Association Training).
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