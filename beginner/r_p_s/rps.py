import random  # Import the random module to generate random choices

# Initialize user and computer scores
user_score = 0
computer_scores = 0

# List of options for the game
options = ["rock", "paper", "scissors"]

# Ask the user if they want to play, convert input to lowercase for case insensitivity
permission = input("Welcome to Rock-Paper-Scissors. Do you want to play? ").lower()

# If the user does not want to play, print goodbye and quit
if permission != "yes":
    print("GoodBye")
    quit()

# If the user wants to play, inform them and start the game
print("Okay Let's Play")

# Main game loop
while True:
    # Ask the user to enter their pick or 'q' to quit, convert input to lowercase
    user_pick = input("Enter your pick OR (Enter q to quit) ").lower()

    # If the user enters 'q', print goodbye and break out of the loop
    if user_pick == "q":
        print("GoodBye")
        break

    # If the user's pick is not valid, continue to the next iteration of the loop
    if user_pick not in options:
        continue

    # Generate a random pick for the computer
    num = random.randint(0,2)
    computer_pick = options[num]
    print(f"Computer Picked: {computer_pick}. ")

    # Determine the winner and update scores accordingly
    if user_pick == "rock" and computer_pick == "scissors":
        print("You Win")
        user_score += 1
        continue

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You Win")
        user_score += 1
        continue

    elif user_pick == "paper" and computer_pick == "rock":
        print("You Win")
        user_score += 1
        continue
    else:
        print("You Loose")
        computer_scores += 1
        continue

# Print final scores
print(f"Your score is {user_score}")
print(f"Computer score is {computer_scores}")
