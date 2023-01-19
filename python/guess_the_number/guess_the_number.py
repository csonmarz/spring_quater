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


def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f' Is guess too high (H), too low(L) or correct (C)??').lower()
        # what this does is we are giving the computer a function where it tries to guess the users number and we then ask the user if our guess is too hig, too low, or just right. Its just like before how the user tries to guess the computers number, but now its reversed.
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(' Yay! The computer guessed your number , {guess} , correctly !')

# The while loop gives the computer an idea is the guess was too high or too low. 
# If too high, the guess will go down by one number
# If too low, the guess will go up by one number
# if correct, it will print our the statement above



        
# what the else statements do is it gives the computer an idea if the guess if going to higher or lower than the random number chosen by the computer.
# if the user guesses the number right, it will go into a statement that will say you got it right, otherwise it will tell you if you guesses to high or low

guess(10)
computer_guess(10)



