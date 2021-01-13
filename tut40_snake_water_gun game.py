import random
print("Welcome to snake_Water_Gun game!!! \n")
print("Total score will be calculated after 10 chances")
player = 0
computer = 0
chance = 0
while chance<10:
    n = int(input("Enter 1 for snake, 2 for water and 3 for gun :"))
    chance = chance+1
    list =["snake","water","gun"]
    choice = random.choice(list)
    if choice=="snake":
        if n==1:
            print("its a tie")
            player=player+0
            computer=computer+0
        elif n==2:
            print("You lost(snake drank the water)")
            computer=computer+1
        else:print("You won(snake shot by gun)")
        player=player+1
    elif choice=="water":
        if n==1:
            print("You won(snake drank the water)")
            player = player+1
        elif n==2:
            print("its a tie")
            player=player+0
            computer=computer+0
        else:print("You lost(gun drowned in water)")
        computer = computer+1
    elif choice=="gun":
        if n==1:
            print("You lost")
            computer=computer+1
        elif n==2:
            print("You won")
            player=player+1
        elif n==3:
            print("Its a tie")
            computer=computer+0
            player=player+0
else:print("Total score of player is",player,"\n" "total score of computer is",computer)






