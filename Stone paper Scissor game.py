from random import randint
def scores(u,c):
    print("\n---Scores---")
    print("User:{}\nComputer: {}".format(u,c))
    print("------------")

print("Welcome to Stone|Paper|Scissor")
n=int(input("Enter 1 to play:\n"))
count_c,count_u,c=0,0,0
if n==1:
    while count_c<5 and count_u<5:
        c+=1
        print("\n    ***Round {}***".format(c))
        ch_u=int(input("Enter 1 to select Stone\nEnter 2 to select Paper\nEnter 3 to select Scissor\n"))
        if ch_u>3 or ch_u<1:
            print("Wrong choice!!! Try again")
            break
        ch_c=randint(1,3)
        if ch_c==1:
            print("I choose Stone")
        elif ch_c==2:
            print("I choose Paper")
        elif ch_c==3:
            print("I choose Scissor")
            
        if ch_u==ch_c:
            print("Draw,Try again")
        elif ch_u==1 and ch_c==3 or ch_u==2 and ch_c==1 or ch_u==3 and ch_c==2:
            print("Uggh!!! I lost this round")
            count_u+=1
            scores(count_u,count_c)
        else:
            print("Yes!!! I win this round")
            count_c+=1
            scores(count_u,count_c)
    print("\n    ***Match Ended***")
    if count_u==5:
        print("Congratulations!!! You won the match, see you next time")
    elif count_c==5:
        print("You lost the match, Better luck next time")


    

