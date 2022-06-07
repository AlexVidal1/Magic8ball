import random
import sys
from random import choice

i = True
turns = 1

want_to_play = input("Type Y to ask a question and shake the magic 8 ball, Type N to not play magic 8 ball: ")

while i:
    if want_to_play.lower() == 'y':
        print(f"Turn #{turns}")
        turns += 1
        print(choice(['yes', 'no', 'maybe', 'It is certain', 'Reply hazy try again', 'Outlook not so good']))
        shake = int(input("Type 1 to ask a question and shake, type 2 to not play anymore: "))
        if shake == 2:
            i = False
    elif want_to_play.lower() == 'n':
        print("Goodbye......For now!")
        sys.exit()
    else:
        print("Follow instructions young one")
        want_to_play = input("Want to play magic 8 ball? Y or N answers only: ")