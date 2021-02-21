while 1:
    from random import randint
    x = input("make your move: ")
    if x == "rock":
        x = 0
    if x == "paper":
        x = 1
    if x == "scissors":
        x = 2
    y = randint (0,2)
    print (f"pc move{y}")
    if y == 0:
        print("rock")
    if y == 1:
        print("paper")
    if y == 2:
        print("scissors")
    if x == y:
        print("draw")
    if x == 1 and y == 0:
        print("you win")
    if x == 1 and y == 2:
        print("you lose")
    if x == 2 and y == 0:
        print("you lose")
    if x == 0 and y == 1:
        print("you lose")
    if x == 2 and y == 1:
        print("you win")
    if x == 0 and y == 2:
        print("you win") 
        
    print("#####################################################")
