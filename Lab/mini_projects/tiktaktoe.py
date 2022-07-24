matrix = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turn=1
def board():
    print(" "+matrix[0]+" | "+matrix[1]+" | "+matrix[2]+" ")
    print("---|---|---")
    print(" "+matrix[3]+" | "+matrix[4]+" | "+matrix[5]+" ")
    print("---|---|---")
    print(" "+matrix[6]+" | "+matrix[7]+" | "+matrix[8]+" ")

def instrBoard():
    print(" (1) | (2) | (3) ")
    print("-----|-----|---")
    print(" (4) | (5) | (6) ")
    print("-----|-----|---")
    print(" (7) | (8) | (9) ")

def player(turn):
    if((turn%2)!=0):
        return "X",p1
    else:
        return "O",p2

def checkVictory():
    if(matrix[0]==matrix[1]==matrix[2]!=" ")or(matrix[3]==matrix[4]==matrix[5]!=" ")or(matrix[6]==matrix[7]==matrix[8]!=" ")or(matrix[0]==matrix[4]==matrix[8]!=" ")or(matrix[6]==matrix[4]==matrix[2]!=" "):
        return True
    else:
        return False

def play(turn):
    sign, name = player(turn)
    print("-"*4,"playing :",name,"-"*4)
    board()
    while(True):
        try:
            moove = int(input("Insert the number of the spot you want to take: "))
            if(moove>=1 and moove<=3):
                if(matrix[moove-1]==" "):
                    matrix[moove-1]=sign
                else:
                    print("That spot is already taken.")
                    continue
            elif(moove>=4 and moove<=6):
                if(matrix[moove-1]==" "):
                    matrix[moove-1]=sign
                else:
                    print("That spot is already taken.")
                    continue
            elif(moove>=5 and moove<=9):
                if(matrix[moove-1]==" "):
                    matrix[moove-1]=sign
                else:
                    print("That spot is already taken.")
                    continue
            else:
                raise JogadaInvalida("must be a number between 1 and 9")
            break
        except:
            print("invalid number!")
            print("Insert a number between 1 and 9")
    if (checkVictory()):
            print("\n"+name,"YOU WON !!!\n")
            board()
            return
    if " " not in matrix:
        print("\nIts a tie !!!\n")
        board()
        return
    play(turn+1)

print("\t### WELCOME TO TIKTAKTOE ###\n")
instrBoard()
print("To play, simply insert the number of the spot were you want to make your moove.\n")
p1 = input("enter the name of player 1 (X): ")
p2 = input("enter the name of player 2 (O): ")
play(turn)

