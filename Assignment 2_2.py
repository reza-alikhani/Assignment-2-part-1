import random
user_action = input("Choose an action (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print("computer chose: ", computer_action)
if user_action == computer_action :
    print("it's a tie")
elif user_action == "rock":
    if computer_action == "paper":
        print("you lose!")
    else:
        print("you win!")
elif user_action == "paper":
    if computer_action == "scissors":
        print("you lose!")
    else:
        print("you win!")
elif user_action == "scissors":
    if computer_action == "rock":
        print("you lose!")
    else:
        print("you win!")
