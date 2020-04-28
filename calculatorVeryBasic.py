"""This is a very basic calculator"""
def calculator():
    while True:
            n1=input('Input first number:\n')
            try:
                if n1.isnumeric():
                    break
                else:
                    print('Error! Enter a number only!')
            except ValueError:
                print('Error! Enter a number only!')
                
    while True:
        op=input('Select operation to make: + - * /\n')
        choices=['+','-','*','/']
        try:
            if op in choices:
                break
            else:
                print('Error! Please select correct operation!')
        except ValueError:
            print('Error! Please select correct operation only!')
            
    while True:
        n2=input('Input second number:\n')
        try:
            if n1.isnumeric():
                break
            else:
                print('Error! Enter a number only!')
        except ValueError:
            print('Error! Enter a number only!')
            
    
    print()
    num1=int(n1)
    num2=int(n2)
    try:        
        if op=='+':
            print('Answer is {}'.format(num1+num2))
        elif op=='-':
            print('Answer is {}'.format(num1-num2))
        elif op=='*':
            print('Answer is {}'.format(num1*num2))
        else:
            print('Answer is {}'.format(num1/num2))
    except ZeroDivisionError:
        print('Cannot divide by zero.')

if __name__=='__main__':
    calculator()
        
    