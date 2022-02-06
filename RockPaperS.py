import random
def playRSP(winner_point):
   cntForUser=0
   cntForPc=0
   user=input("'r'for rock,'p'for paper,'s' for scissor:").lower()
   comp=random.choice(['r','p','s'])
   while cntForUser!=winner_point and cntForPc!=winner_point:
        print(f'Pc:{comp}')
       
        if user==comp:
           print("No points for both sides")
        elif user=='r' and (comp=='s' or comp=='p'):
            cntForUser+=1
        elif  comp=='r' and (user=='s' or user=='p'):
             cntForPc+=1
        elif user=='s' and comp=='p':
            cntForUser+=1
        elif comp=='s' and user=='p':
            cntForPc+=1
        else:
            print("invalid character!")
        print(f"Pc:{cntForPc} vs You:{cntForUser}")
        if cntForUser==winner_point or cntForPc==winner_point:
            break
           
        user=input("'r'for rock,'p'for paper,'s' for scissor:")
        comp=random.choice(['r','p','s'])
   if cntForPc==winner_point:
       print(f'Sorry,Winner is Computer who reached to {winner_point} points,You lose...')
   else:
       print(f'Congrats, You are the winner , reached to {winner_point} points')


winner=int(input("Type winner point:"))
playRSP(winner)

again=input("Do you wanna play again(y/n)?:").lower()
while again=='y':
    print("*****New game****")
    winner=int(input("Type winner point:"))
    playRSP(winner)
    again=input("Do you wanna play again?").lower()

print("****GAME OVER :(****")   

       
         
        
            
    
    
