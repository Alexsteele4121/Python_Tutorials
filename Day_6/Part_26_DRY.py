# PART 26: DRY principle

# "Don't repeat yourself" (DRY)
# The idea is that there should only ever be one copy of any important piece of information.
# If you find the same chunk of code in multiple spots than your code is probably due for some refactoring.

# Example of code that isn't DRY:

correct_guesses = []
while correct_guesses != [1, 5, 7, 8]:
    guess = input('Guess a digit: ')
    try:
        guess = int(guess)
    except ValueError:
        print('Invalid Entry')
        continue
    if guess in [1, 5, 7, 8]:
        print('Correct!')
        if guess not in correct_guesses:
            correct_guesses.append(guess)
    elif guess not in [1, 5, 7, 8]:
        print('Nope! Try again!')

print('You got all the digits!')


# DRY code:
