import random
values = ("rock","paper","scissors")
playing = True

while playing:
    player = None
    computer = random.choice(values)

    while player not in values:
        player = input("Enter a choice (rock ,paper ,scissors):")
    print(f"player:{player}")
    print(f"computer:{computer}") 

    if player == computer:
        print(" It is a draw")
        
    elif player == "rock" and computer == "scissors":
        print("You win!")
        
    elif player == "scissors" and computer == "paper":
        print("You win!")
        
    elif player == "paper" and computer == "rock":
        print("You win!")
        
    else:
        print("You lose!")
        
    play_again = input("Do you want play another game?(Yes/No)")
    if not play_again == "yes":
        playing = False
        
print("Thanks for playing!")