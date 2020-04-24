import random

def get_attempts():
    while True:
        attempts=input('How many attempts do you want? (3-5 only)\n')
        try:
            attempts=int(attempts)
            if 2<attempts<6:
                return attempts
            else:
                print('{} is not in the range of 3 to 5. Please select again.'.format(attempts))
        except ValueError:
            print('{} is not an integer in the range of 3 to 5. Please select again.'.format(attempts))
            
def word_length():
    while True:
        wordlength=input('How many words do you want? (minimum 3)\n')
        try:
            wordlength=int(wordlength)
            if wordlength>2:
                return wordlength
            else:
                print('Please select again. Minimum of length 3')
        except ValueError:
            print('{} is not an integer. Please select again.'.format(wordlength))
        
def get_random(wordlength):
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    random_numbers=random.sample(range(0,len(letters)),wordlength)
    words=[]
    for numbers in random_numbers:
        words.append(letters[numbers])
    
    return words

def guess():
    attempts=get_attempts()
    wordlength=word_length()
    words=get_random(wordlength)
    word=''.join(words)
    guessed=[]
    while attempts and words:
        letterguess=input('Guess a letter:\n').lower()
        if letterguess.isalpha():
            if letterguess in guessed:
                print('That letter has already been guessed. Select another.')
            elif letterguess in words:
                print('Correct! {} is in word.'.format(letterguess))
                guessed.append(letterguess)
                words=[letters for letters in words if letters!=letterguess]
            else:
                attempts-=1
                if not attempts:
                    print('Wrong letter is selected.')
                else:
                    print('Wrong letter is selected. Please try again. Remaining attempts: {}'.format(attempts))
                    guessed.append(letterguess)
        else:
            print('Please input a letter.')
            
    score(attempts,word)
    
    again=input('Would you like to try again? [y/n]\n').lower()
    return again=='y'

def score(attempts,word):
    if not attempts:
        print()
        print('You lost. Better try next time.')
        print('The correct word is "{}"'.format(word))
    else:
        print('Congratulations! You won the game.')
    
if __name__ == '__main__':
     while guess():
         print()               
                
                
                
                
                
                
                
    