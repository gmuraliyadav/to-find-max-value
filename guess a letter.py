from random import randint

print("wecome to guessing game\nI thing number in 1 to 100")
easy_mode = 10
hard_mode = 5

def check_ans(ask, val):
    if ask > val:
        print("Val is too high")
    else:
        print(f"low value \n you got it  the answer was {val}")
        
    
def difficult_mode():
    global turns 
    level_ask = input("choose 'easy' or 'hard'")
    if level_ask =="easy":
        return  easy_mode
    else:
        return hard_mode
        


val = randint(1,100)

ask = int(input("make a guess"))
turns = difficult_mode()
print(f"you have ramain {turns}")

print("")






