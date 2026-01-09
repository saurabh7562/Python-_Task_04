import random
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "===== Rock Paper Scissors — Best of 5 =====")

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
round_number = 1

print(Fore.YELLOW + "\nFirst to 3 points wins the game!")

while user_score < 3 and computer_score < 3:

    print(Fore.MAGENTA + f"\n--- Round {round_number} ---")
    print(Fore.WHITE + "Choose: rock / paper / scissors")

    user = input(Fore.BLUE + "Your choice: ").lower()

    if user not in options:
        print(Fore.RED + "Invalid choice! Try again.")
        continue

    computer = random.choice(options)

    print(Fore.GREEN + f"\nYou chose: {user}")
    print(Fore.RED + f"Computer chose: {computer}")

    # Game logic
    if user == computer:
        print(Fore.YELLOW + "Result: It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print(Fore.GREEN + "Result: You win this round! ")
        user_score += 1
    else:
        print(Fore.RED + "Result: Computer wins this round ")
        computer_score += 1

    print(Fore.CYAN + f"\nScore -> You: {user_score} | Computer: {computer_score}")

    round_number += 1

# Final result
print(Fore.YELLOW + "\n===== Final Result =====")

if user_score > computer_score:
    print(Fore.GREEN + " You won the game! Great job!")
else:
    print(Fore.RED + " Computer won the game. Better luck next time!")

print(Fore.CYAN + "\nThanks for playing!")

