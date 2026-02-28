import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("\n--- Welcome to the Guessing Logic Challenge! ---")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} tries.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print(" Invalid input! Please enter a whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print(" Higher!")
        elif guess > secret_number:
            print(" Lower!")
        else:
            print(f" Correct! You found it in {attempts} attempts.")
            return True 

    print(f" Game Over! The number was {secret_number}.")
    return False 


if __name__ == "__main__":
    while True:
        play_game() 
        
       
        print("\n" + "-"*30)
        choice = input("Do you want to play again? (Enter 'Y' for Yes or 'Q' to Quit): ").strip().upper()
        
        if choice == 'Q':
            print("Thanks for playing! Goodbye.")
            break
        elif choice == 'Y':
            print("Restarting...")
            continue 
        else:
            print("Invalid choice, but let's play again anyway!")

