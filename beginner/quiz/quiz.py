#Greeting the user
print("Welcome to Computer Quiz Game")
score = 0

#Asking if user want to play
play = input("Do you want to play?(yes or no) ").lower()
if play != "yes":
    quit()

print("Okay Let's Play :) ")

#Asking Questions. (it's okay to use same variable for different question after a if statement)
#Q1.
answer = input("Q1. what is 1+1 equals to? ")
if answer == "2":
    print("Correct")
    score += 1
else:
    print("Incorrect")
#Q2.
answer = input("Q2. what is 5*6 equals to? ")
if answer == "30":
    print("Correct")
    score += 1
else:
    print("Incorrect")
#Q3.
answer = input("Q3. what is 9*9 equals to? ")
if answer == "81":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f"score is {score} out of 3")