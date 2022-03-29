import time
import os
import random
score = [0,0]
game_on = True
x= list(range(1,21))
l=["A","B","C","D","E","F","G","H","I","J"]*2
random.shuffle(l)

def check_list1(num1, num2,player):
    global score
    if l[num1 - 1] == l[num2 - 1]:
        score[player] += 1
        print("Player "+str(player+1)+" score:", score[player])
        x[num2 - 1] = "*"
        x[num1 - 1] = "*"
        l[num2 - 1] = "*"
        l[num1 - 1] = "*"
    return ()

while game_on == True :
    os.system("cls")   #this block work must be run at console application or visual studio code
    print(score[0]," ",score[1])
    print(l)
    time.sleep(10)
    os.system("cls")
    print(score[0]," ",score[1])
    print(x)
    num1,num2=input("Player1,Please enter 2 numbers from 1 to 20:").split(" ")
    num1 = int(num1)
    num2 = int(num2)

    while num1>20 or num2 >20  or x[num1-1]=="*" or x[num2-1]== "*":
        num1,num2=input("invalid input ,please enter 2 numbers from 1 to 20: ").split(" ")
        num1 = int(num1)
        num2 = int(num2)
    check_list1(num1,num2,0)
    #if game end break
    if score[0]+score[1]==10:
        break

    num3,num4=input("Player2,Please enter 2 numbers from 1 to 20: ").split(" ")
    num3 = int(num3)
    num4 = int(num4)

    while num3>20 or num4>20 or x[num3-1]=="*" or x[num4-1]=="*":
        num3,num4 = input("invalid number, Please enter 2 numbers from 1 to 20: ").split(" ")
        num3 = int(num3)
        num4 = int(num4)
    check_list1(num3,num4,1)
    #if game end break
    if score[0]+score[1]==10:
        break


if score[0]> score[1]:
    print("Player1 Won!")
elif score[0]<score[1]:
    print("Player2 Won!")
else:
    print("Game draw!") 

