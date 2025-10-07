
# Author :: Eloise Ridder-Strickland
# PURPOSE :: Text Based Interface Logic.

def option_1():
    print("You selected Option 1.")

def option_2():
    print("You selected Option 2.")

def option_default():
    print("Invalid option. Please try again.")

while True:
    print("\n ========== MAIN MENU =========")
    print("Press any number to begin")
    print("1. Standard Identification Game")
    print("2. Shuffle Identification Game")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        option_1()
    elif choice == '2':
        option_2()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        option_default()