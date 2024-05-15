def main():
    print ("wlecome to Dice Game")
    while True:
        try:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = int(input("\n What would you like to do? (1-3)"))
            if choice == 1:
                #register() 
                print("3. Exit")
            elif choice == 2:
                #login()
                print("3. Exit")
            elif choice == 3:
                #exit
                print("Exiting the game. Goodbye!")
                break
            else:
                print("invalid input.")
        except ValueError:
            print("ValueError. Please input a number within the choices.")

def dicegame_main():
    print (f"Welcome") # {username}")
    while True:
        try:
            print("Menu : ")
            print("1. Start")
            print("2. View Rankings")
            print("3. Log Out")
            choice = int(input("Enter your choice, or leave blank to cancel : "))
            if choice == 1:
                #start()
                pass
            elif choice == 2:
                #rankings()
                pass
            elif choice == 3:
                print("Logging out....")
                print("Thanks for playing!")
                #logout()
        except ValueError:
            print("ValueError. Please input a number within the choices.")



if __name__ == "__main__":
    main()