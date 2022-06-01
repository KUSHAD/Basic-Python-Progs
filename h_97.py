import random

random_number = random.randint(1, 9)
chances = 5

while chances > 0:

    user_input = int(raw_input("Guess the number between 1 and 9 :-"))

    if (user_input != random_number):

        if(user_input > random_number):
            diff = user_input - random_number
            print('You are ', diff, ' more than the correct number')

        elif(user_input < random):
            diff = random_number - user_input
            print('You are ', diff, ' less than the correct number')

    else:
        print("You guessed the correct number")

    chances = chances - 1

    if (chances == 0):
        print("You are out of chances. The correct number was ", random_number)
