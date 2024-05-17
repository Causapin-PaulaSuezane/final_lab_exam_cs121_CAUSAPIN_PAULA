
from utils.user_manager import UserManager
from utils.dice_game import DiceGame

#main function
def main():
    user_manager = UserManager()
    dice_game = DiceGame()
    print("Welcome to Dice Game")
    while True:
        try:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("\nWhat would you like to do? (1-3) : ")
            
            if choice == "1": #registration
                print("\nRegistration:")
                username = input("Enter username (leave blank to cancel): ")
                if not username:  #if user entered with no any input, it'll cancel
                    print("Registration canceled.")
                    continue
                password = input("Enter password (leave blank to cancel): ")
                if not password:  
                    print("Registration canceled.")
                    continue
                if user_manager.register(username, password):
                    print("Registered successfully.")
                    
            elif choice == "2": #login
                print("\nLogin:")
                username = input("Enter username (leave blank to cancel): ")
                if not username:  
                    print("Login canceled.")
                    continue
                password = input("Enter password (leave blank to cancel): ")
                if not password: 
                    print("Login canceled.")
                    continue
                if user_manager.login(username, password):
                    dice_game.current_user = username
                    print("Login successfully!")
                    dice_game.menu()
                else:
                    print("Invalid username or password.")
                    
            elif choice == "3": #exit
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("ValueError. Please input a number within the choices.")


if __name__ == "__main__":
    main()
