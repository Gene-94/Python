import random

print("I am thinking of number between 0 and 100, can you guess what it is?")
print("\t( type 'exit' to give up )")
secret = random.randint(0,100)
count = 0
while True:
    guess = input("guess > ")
    if(guess == "exit"):
        break
    else:
        try:
            guess = int(guess)
            count = count + 1
            if(guess > secret):
                print("Too high !")
            elif(guess < secret):
                print("Too low !")
            else:
                print("\nYou guessed it! And only in",count,"guesses...")
                break            
        except:
            print("Not a number! Try again.")