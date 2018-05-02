
import ex35
import random
import sys


def Croom():
    print "this is a A room"
    print "you need to guess a nummber betwwen (0,10)to exit,and you have 3 tries"
    num=random.randint(0,10)
    tries=1
    while tries <=4 :  
        guess=raw_input("please input your guess num > ")
        g=int(guess)
        if g!= num:
            left=4-tries
            print "You are wrong and you have %d lifes left" %left
        else :
            print "Good ,you win, you can go "
            Droom()
            break
        if tries==4 and g!=num:
            ex35.dead("You lost your lives the right num is %d " %num) 
        tries+=1

def Droom():
    words=[]
    print "You enter a new room "
    print "I want to play a game with you"
    print "You need to sort the list"
    print ("Please input three words")
    n=0
    while n<3:
        word=raw_input("> ")
        words.append(word)
        n+=1
    words2=sorted(words)
    print "after sorting what is the second word ? "
    getword=raw_input(">=")
    if words[2]==getword:
        print "Yes you win the game "
        print "The sorted word list is",words2
        print "Do you want to play again? Y/N"
        choice=raw_input("> ")
        if choice=='Y':
            startA()
        elif choice=='N':
            print "Bye"
            sys.exit(0)
    else:
        ex35.dead("you dead ")
    
    

def startA():
    print "You found a tree house in the forest "
    print "There are 3 rooms Which room will you go first A,B,C  "
    while True:
        choose=raw_input("> ")
        if choose=="A":
            ex35.bear_room()
        elif choose=='B':
            ex35.cthulhu_room()
        elif choose=='C':
            Croom()
        else :
            print "I can't understand "
        
startA()
