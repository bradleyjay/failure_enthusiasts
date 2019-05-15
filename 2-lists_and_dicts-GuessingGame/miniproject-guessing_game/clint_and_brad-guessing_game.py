import random

stop = False

def guessing_game():

    correct_ans = random.randint(1,3)
    
    while True:

        guess = input("I'm thinking of a number between 1 and 100. Can ya guess it?\n" )
      
        # checks

        if guess.isdigit() == False:
            print("get ouuuuuut")
        elif int(guess) < correct_ans:
            print("Too small!")
        elif int(guess) > correct_ans:
            print("Too beeeeeeg")
            return "Great job, you're smahter than a computah"


while not stop:
    message = guessing_game()
    response = input("Wanna play again? y/n")

    if response == 'n':
        stop = True