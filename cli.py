from random import randint
import matplotlib.pyplot as plt
import numpy as np

# Prompts the user for a guess.
# Returns the guess as an integer
def get_user_guess(prompt):
    return int(input(prompt + "\n").strip())

# runs the guessing game and returns the number of tries it took for the correct number to be reached
def run_guessing_game(game_mode):
    my_random = randint(1, 100)
    if game_mode == 'User':
        user_guess = get_user_guess("Guess a number between 1 and 100")
        user_count = 1
        print(user_guess)

        while user_guess != my_random:
            user_count += 1
            if my_random > user_guess:
                print("Your guess is too low!")
            else:
                print("Your guess is too high!")
            user_guess = get_user_guess("Try again")

        print("Your guess is correct!")
        print(f"It took you {user_count} tries to guess correctly!")
        return user_count
    elif game_mode == 'Bisect':
        # machine plays the game
        machine_count = 1
        low = 1
        high = 100
        machine_guess = int((high - low) / 2 + low)

        while machine_guess != my_random:
            # print(machine_guess)
            machine_count += 1
            if my_random > machine_guess:
                # print(f"Your guess is too low! {machine_guess}")
                low = machine_guess
            else:
                # print(f"Your guess is too high! {machine_guess}")
                high = machine_guess
            if machine_guess == 99:
                machine_guess = 100
            else:
                machine_guess = int((high - low) / 2 + low)

        # print("Your guess is correct!")
        # print(f"It took you {machine_count} tries to guess correctly!")
        return machine_count
    elif game_mode == 'Linear':
        pass
    elif game_mode == 'Random':
        pass
    else:
        raise RuntimeError(f"I don't know this game mode {game_mode}")

try_counts = dict()
for i in range(1_000_000):
    tries = run_guessing_game('Bisect')
    if tries in try_counts:
        try_counts[tries] += 1
    else:
        try_counts[tries] = 1
print(try_counts)
print(try_counts.keys())
print(try_counts.values())

plt.bar(try_counts.keys(), try_counts.values(), 1.0, color='g')
plt.show()