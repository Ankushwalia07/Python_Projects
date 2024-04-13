import random

ask = input("Do you want to play the number guessing Game? ").lower()
if ask != 'yes':
    quit()

print("Okay Let's Play")

top_range = input("Enter the Upper Bound for the Guessing Number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Enter a positive number next time.")
        quit()

else:
    print("Enter a number next time.")
    quit()

num = random.randint(0,top_range)
guesses = 0
while True:
    guesses += 1
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
    if guess == num:
        print(f"You've guessed the right number, the number is: {num}")
        break
    else:
        if guess > num:
            print("You're above the number")
        else:
            print("You're under the number")


print(f"IN {guesses} guesses.")