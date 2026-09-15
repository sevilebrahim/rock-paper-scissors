import random

choices = ["rock", "paper", "scissors"]

you_score = 0
computer_score = 0

for round_number in range(4):

    you = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer:", computer)

    if you == computer:
        print("Draw!")

    elif (
        (you == "rock" and computer == "scissors")
        or (you == "paper" and computer == "rock")
        or (you == "scissors" and computer == "paper")
    ):
        you_score += 1
        print("You win this round!")

    else:
        computer_score += 1
        print("Computer wins this round!")

    print("----------------")

print("YOU:", you_score)
print("COMPUTER:", computer_score)

if you_score > computer_score:
    print("YOU WIN THE GAME!")

elif computer_score > you_score:
    print("YOU LOSE!")

else:
    print("GAME DRAW!")
