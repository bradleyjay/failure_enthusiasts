import random

game_on = True

random_number = random.randint(1,100)


print("Hello!  I'm thinking of a number between 1 and 100.  Can you guess it?")



while game_on:

    player_guess = int(input("Guess a number between 1 and 100 \n"))
    
    if player_guess == random_number:
        print("You got it!  The number was " + str(random_number) + "!")
        game_on = False
    elif player_guess < random_number:
        print("Too Low!")
    else:
        print("Too High!")
    
print("Bye!")
