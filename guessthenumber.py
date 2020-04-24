"""A simple game where you guess the number from range of 0 to 20"""
import random

#generate the random number
def create_number():
    random_number=random.randint(0,20)
    return random_number

#guess the number
def guess(random_number):
    while True:
        guessed=input('Guess the number from 0-20: \n')
        try:
            guessed=int(guessed)
            if 20<guessed<0: 
                print('Guessed number is out of range.')
            elif guessed<random_number:
                print('Wrong! Guessed number is too low.')
            elif guessed>random_number:
                print('Wrong! Guessed number is too high.')
            else:
                print('Congratulations! You guessed the correct number.')
                return guessed
        except ValueError:
            print('Please input a number between 0-20.')

def game():
    random_number=create_number()
    guessed=guess(random_number)
    again=input('Do you wish to continue? [y/n] \n').lower()
    return again=='y'

if __name__=='__main__':
    while game():
        print()
                    