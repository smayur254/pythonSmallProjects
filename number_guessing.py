import random

pc_num = random.randrange(0,100)
count = 10
user_score = 0
pc_score = 0
print("Welcome to number guesing game.")
print("Rules for the game.")
print("You have 10 chances to win.")
print("If pc guess bigger number than yours pc win the round")

while count>0:
    try:
        user_ip = int(input("Enter yout number: "))
        if user_ip == pc_num:
            count-=1
            user_score+=1
            pc_score+=1
            print("You are winner.")
            print("Chances left.", count)
            print("Score of Pc: ",pc_score)
            print("Score of You: ",user_score)
            print()
            break
        elif user_ip < pc_num:
            pc_score+=1
            count-=1
            print("Lower number. Please guess higher.")
            print("Chances left.", count)
            print("Score of Pc: ",pc_score)
            print("Score of You: ",user_score)
            print()
        else:
            pc_score+=1
            count-=1
            print("Higher number. Please guess lower.")
            print("Chances left.", count)
            print("Score of Pc: ",pc_score)
            print("Score of You: ",user_score)
            print()
        
            
    except Exception as e:
        print(e)

if count == 0:
    print("try again next time")