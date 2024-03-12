from random import *

print("----------ROCK PAPER SCISSORS----------")
ch=["Rock","Paper","Scissors"]

u=0
s=0

while True:
    uch=input("Rock / Paper / Scissors : ")
    sch=choice(ch)
    if uch==sch:
        res="TIE!!"
    elif uch=="Rock" and sch=="Scissors" or uch=="Paper" and sch=="Rock" or uch=="Scissors" and sch=="Paper":
        res="YOU WON!"
        u+=1
    elif sch=="Rock" and uch=="Scissors" or sch=="Paper" and uch=="Rock" or sch=="Scissors" and uch=="Paper":
        res="COMPUTER WON!"
        s+=1
    else:
        print("Invalid Choice\n")
        pass
    print("Your choice:"+uch+"\t\t"+"Computer's choice:"+sch)
    print("** {} **".format(res))
    print("Score:\n"+"You:"+str(u)+"\tComputer:"+str(s))
    pa=input("Want to play again? (Yes/No): ").lower()
    if pa=="yes":
        print()
        pass
    else:
        print("----------Thanks for playing.----------\n")
        break
