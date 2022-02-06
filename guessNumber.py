import random

def guess(x):
    random_num=random.randint(1,x)
    guess=0
    while guess!=random_num:
        guess=int(input(f"Guess a number betten 1 and {x}:"))
        if guess< random_num:
            print("Sorry,it is smaller than the lucky number")
        elif guess>random_num:
            print("Sorry,It is bigger than the lucky number")
    print("Congrats!,You find the lucky number...")
            


def compt_guess(x):
    low=1
    high=x
    feedback=' '
    while feedback!='c':
        if low!=high:
           guess=random.randint(low,high) 
        else:
             guess=low 
        feedback=input(f'Is {guess} too high(H) or low(L),or correct(C)').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"Congrats Computer found the lucky number({guess})!")
    
    
compt_guess(5)
             
        
        
        
        
    
        