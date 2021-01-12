import random
import re

while 1 < 2:
    print("Rock, Paper, Scissors - Shoot!")
    Player = input("Please choose a letter for your weapon [R]ock, [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", Player):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
        continue

    print("You chose: " + Player)
    choices = ['R', 'P', 'S']
    opponent = random.choice(choices)
    print("I chose: " + opponent)
    if opponent == str.upper(Player):
        print("Tie! ")
    elif opponent == 'R' and Player.upper() == 'S':
        print("Scissors beats rock, I win! ")
        continue
    elif opponent == 'S' and Player.upper() == 'P':
        print("Scissors beats paper! I win! ")
        continue
    elif opponent == 'P' and Player.upper() == 'R':
        print("Paper beat rock, I win! ")
        continue
    else:
        print("You win!")
