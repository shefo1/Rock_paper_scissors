# Rock_paper_scissors game
# ask the user enter the  (r for rock, p for paper, s for scissors)
# if user choose the (rock and pc choose the scissors) (user choose the scissors pc choose paper )(user choose paper pc choose rock)
#  the user is win
# else pc win/ user lose

import random


user = (input ("choose :r for rock, p for paper, s for scissors\n : "))
pc = random.choice(["r",'p','s'])



if user == pc:
    print("your choose is",user)
    print("pc choose a ", pc)
    print ("It's a tie!")

elif( user == 'r' and pc == 's') or   (user == 's'and pc == 'p' ) or (user == 'p'and pc == 'r'):
    print("your choose is",user)
    print("pc choose a ", pc)
    print ('You won!') 

elif( user != 'r'or's'or 'p') :
    print ('Error!! \n  Enter the correct choice')

else:
    print("your choose is",user)
    print("pc choose a ", pc)
    print("pc is won")    
