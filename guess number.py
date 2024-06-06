import random

def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

if __name__ == "__main__":
    guess_the_number()
