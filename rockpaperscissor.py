"""A game of rock, paper, scissors"""
import random

#Choose number of attempts
def attempts():
    while True:
        att=input('Please select if game is maximum score of 3 or 5: Enter 3 or 5\n')
        try:
            att=int(att)
            if att==3 or att==5:
                return att
            else:
                print('Please enter either 3 or 5 only.')
        except ValueError:
            print('Please enter the number 3 or 5 only.')
                
#Choose the opponent choice
def opponent():
    choices=['rock','paper','scissor']
    opp=random.choice(choices)
    return opp

#Play the game
def play(att):
    opponent_score=0
    score=0
    choices=['rock','paper','scissor']
    opp=opponent()
    while score<att and opponent_score<att:
        player=input('Select rock, paper, or scissor: \n').lower()
        try:
            if not player.isalpha() or player not in choices:
                print('Please select rock, paper, or scissor only!')
            if player==opp:
                print('It is a draw.')
            elif (player=='rock' and opp=='paper') or (player=='paper' and opp=='scissor') or (player=='scissor' and opp=='rock'):
                opponent_score+=1
                print('You lost. Opponent chose {}.'.format(opp))
                print('Score is You:{}, Opponent:{}'.format(score,opponent_score)) 
            elif (player=='rock' and opp=='scissor') or (player=='paper' and opp=='rock') or (player=='scissor' and opp=='paper'):
                score+=1
                print('You won. Opponent chose {}.'.format(opp))
                print('Score is You:{}, Opponent:{}'.format(score,opponent_score)) 
            opp=opponent()
        except ValueError:
            print('Please select rock, paper, or scissor only!')
            
    if opponent_score>score:
         print('You lost!')
    else:
         print('You won!')
         
    again=input('Play again? [y/n]\n').lower()
    return again=='y'    
         
def game():
    att=attempts()
    return play(att)

if __name__=='__main__':
    while game():
        print()
    
  