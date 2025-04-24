import random

def generate_number():
    return random.randint(1, 100)

def play_game(attempts):
    c_value = generate_number()
    for i in range(attempts):
        while True:
            try:
                u_value = int(input("🔢 Make a guess (1–100): "))
                break
            except ValueError:
                print("⚠️ Please enter a valid number!")

        if u_value == c_value:
            print("🎉 Your guess is right!!")
            return
        elif u_value > c_value:
            print("📉 Too high.")
        else:
            print("📈 Too low.")

        remaining = attempts - (i + 1)
        if remaining > 0:
            print(f"❗ You have {remaining} attempts remaining.\n")
        else:
            print(f"💥 No attempts left. You lost the game. The correct number was {c_value}.")

def game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        attempts = 10
    elif level == 'hard':
        attempts = 5
    else:
        print("⚠️ Invalid difficulty level. Try again.")
        return

    play_game(attempts)

while True:
    game()
    again = input("\n🔁 Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing! Goodbye!")
        break
