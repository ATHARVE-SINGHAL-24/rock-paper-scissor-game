# print("WELCOME TO ROCK,PAPER AND SCISSORS GAME!!")

# import random

# emoji={"r":"🧱","p":"📜" , "s":"✂"}
# choices=("r","p","s")             #stored in tuple

# while True:
#     user_choice=str(input("Rock,paper or scissors?(r/p/s): "))
#     if(user_choice not in choices):
#         print("invalid choice!")
#         continue


#     computer_choice=random.choice(choices)

#     print("you choose :",emoji[user_choice])
#     print("computer choose :",emoji[computer_choice])

#     if(user_choice==computer_choice):
#         print("tie!")

#     elif(
#         (user_choice=="r" and computer_choice=="s") or
#         (user_choice=="s" and computer_choice=="p") or
#         (user_choice=="p" and computer_choice=="r")):
#         print("you win")


#     else:
#         print("you lose")


#     may_continue=str(input("continue?(y/n): "))
#     if(may_continue=="n"):
#         break








#LEVEL 2 


# print("WELCOME TO ROCK,PAPER AND SCISSORS GAME!!")

# import random

# emoji={"r":"🧱","p":"📜" , "s":"✂"}        #maped with sign
# choices=("r","p","s")             #stored in tuple

# user_winning=0
# computer_winning=0

# while True:
#     user_choice=str(input("Rock,paper or scissors?(r/p/s): "))
#     if(user_choice not in choices):
#         print("invalid choice!")
#         continue


#     computer_choice=random.choice(choices)

    

#     print("you choose :",emoji[user_choice])
#     print("computer choose :",emoji[computer_choice])



#     if(user_choice==computer_choice):
#         print("tie!")
#         computer_winning+=0
#         user_winning+=0        
#         print("you win:",user_winning ,"computer win:", computer_winning)



#     elif(
#         (user_choice=="r" and computer_choice=="s") or
#         (user_choice=="s" and computer_choice=="p") or
#         (user_choice=="p" and computer_choice=="r")):
#         print("you win")
#         user_winning+=1
#         print("you win:",user_winning ,"computer win:", computer_winning)

#     else:
#         print("you lose")
#         computer_winning+=1        
#         print("you win:",user_winning,"computer win:", computer_winning)




#     may_continue=str(input("continue?(y/n): "))
#     if(may_continue=="n"):
#         break









#LEVEL 3




print("WELCOME TO ROCK,PAPER AND SCISSORS GAME!!")

import random

emoji={"r":"🧱","p":"📜" , "s":"✂"}        #maped with sign
choices=("r","p","s")             #stored in tuple

user_winning=0
computer_winning=0

count=1
while count<=5:
    user_choice=str(input("Rock,paper or scissors?(r/p/s): "))
    if(user_choice not in choices):
        print("invalid choice!")
        continue


    computer_choice=random.choice(choices)

    

    print("you choose :",emoji[user_choice])
    print("computer choose :",emoji[computer_choice])



    if(user_choice==computer_choice):
        print("tie!")
        computer_winning+=0
        user_winning+=0        
        print("you win:",user_winning ,"computer win:", computer_winning)
        count+=1



    elif(
        (user_choice=="r" and computer_choice=="s") or
        (user_choice=="s" and computer_choice=="p") or
        (user_choice=="p" and computer_choice=="r")):
        print("you win")
        user_winning+=1
        print("you win:",user_winning ,"computer win:", computer_winning)
        count+=1

    else:
        print("you lose")
        computer_winning+=1        
        print("you win:",user_winning,"computer win:", computer_winning)
        count+=1

if(user_winning>computer_winning):
    print("congratulation,you won the game")
elif(user_winning==computer_winning):
    print("The game is draw")
else:
    print("sorry, you have lost the game.Try again!")

    

    











