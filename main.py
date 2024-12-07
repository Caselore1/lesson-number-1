import random

name = 'Daniil'
id = 'USA9023483578'
balance1 = 156
balance2 = 60.3
boolean = False #True
#print(bool(0))
print('Hello ' + name)
print('Ur id is' + id)
##if score == 200:
#    print('You win')
#else:
 #   print('You lose')

lifes = 3
win_var = random.randint(0, 16)
check = int(input('Enter ur number'))

while lifes != 1:
    if check == win_var:
        print('You win')
        break
    elif check > win_var:
        print('U number is more than need')
    elif check  < win_var:
        print('Ur number is less that need')
    else:
        print('Wrong data input')

    lifes = lifes - 1
else:
    print('You lose')

