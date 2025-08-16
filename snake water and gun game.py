'''
1 for snake
-1 for water 
0 for gun
'''

import random 
computer =random.choice([1,-1,0])
yourstr=input("Enter your choice :")
yourDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you=yourDict[yourstr]

print(f"your choice{reverseDict[you]}\n computers choice {reverseDict[computer]}")

if (computer == you):
    print("its draw ")
else:
    if(computer == 1 and you == -1):
        print("you loose ")
    elif(computer == 1 and you == 0):
        print("you loose ")
    elif(computer == -1 and you == 1):
        print("you win ")
    elif(computer ==-1 and you == 0):
        print("you loose ")
    elif(computer == 0 and you == 1):
        print("you win ")
    elif (computer == 0 and you == -1):
        print("you win ")
    else:
        print("something went wrong ")