from utils.user_manager import UserManager
from utils.dice_game import DiceGame

def main():
    user_manager = UserManager()
    dice_game = DiceGame()
    
    print ("Welcome to Dice Game")
    while True:
        try:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = int(input("\n What would you like to do? (1-3)"))
            if choice == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if user_manager.register(username, password):
                    print("Registered Successfully.")
                else:
                    print("Username already exist.")
            elif choice == 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if user_manager.login(username, password):
                    dice_game.current_user = username
                    dice_game.menu()
            elif choice == 3:
                print("Exiting the game. Goodbye!")
                break
            else:
                print("invalid input.")
        except ValueError:
            print("ValueError. Please input a number within the choices.")



if __name__ == "__main__":
    main()