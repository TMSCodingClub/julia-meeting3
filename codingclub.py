import random

score = 0

def decide(input):
    if(input == "yes"):
        return True
    elif(input == "no"):
        return False

def randomCard():
    card = random.randint(1,13)
    if(card>10):
        return 10
    else:
        return card

while(True):
    print("Your score is ",score)
    words = input()
    if(decide(words)):
        print("You get a card")
        score = score + randomCard()
    else:
        print("No.")

    if(score>21):
        while(True):
            print("You lost")

hello change
