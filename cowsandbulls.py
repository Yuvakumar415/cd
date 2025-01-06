import random

def generate_number():
    """Generates a 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def get_cows_and_bulls(secret, guess):
    """Calculates the number of cows and bulls."""
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return cows, bulls

def play_game():
    print("Welcome to the Cows and Bulls Game!")
    print("I have generated a 4-digit number. Try to guess it!")
    print("For each guess, I will tell you how many Cows and Bulls you have.")
    print("Cows: Correct digits in the wrong position.")
    print("Bulls: Correct digits in the correct position.")
    print("Type 'exit' to quit the game.")
    
    secret_number = generate_number()
    attempts = 0
    
    while True:
        guess = input("\nEnter your guess (4 unique digits): ")
        
        if guess.lower() == 'exit':
            print(f"The secret number was {secret_number}. Better luck next time!")
            break
        
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input. Please enter a 4-digit number with unique digits.")
            continue
        
        attempts += 1
        cows, bulls = get_cows_and_bulls(secret_number, guess)
        
        print(f"Cows: {cows}, Bulls: {bulls}")
        
        if bulls == 4:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

if _name_ == "_main_":
    play_game()