import random
#this function tells the code to grab any random number 

def guess(x):
    random_number = random.randint(1,x)
    guess= 0
    while guess != random_number:
        guess= int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. You are too low!')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrat. You have guessed the right number {random_number} correctly!')


guess(10)
        
# what the else statements do is it gives the computer an idea if the guess if going to higher or lower than the random number chosen by the computer.
# if the user guesses the number right, it will go into a statement that will say you got it right, otherwise it will tell you if you guesses to high or low

